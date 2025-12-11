"""
Необходимые библиотеки:
pip install sounddevice numpy scipy pygame vosk
"""

from __future__ import annotations
import datetime as _dt
import os
import queue
import threading
import wave
from dataclasses import dataclass
from pathlib import Path
from typing import Optional
import numpy as np
import pygame
import sounddevice as sd
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

try:
    from vosk import KaldiRecognizer, Model

    _VOSK_AVAILABLE = True
except ImportError:  
    KaldiRecognizer = Model = None  
    _VOSK_AVAILABLE = False


SAMPLE_RATE = 44_100
CHANNELS = 1
RECORDINGS_DIR = Path("recordings")
RECORDINGS_DIR.mkdir(exist_ok=True)


@dataclass
class Recording:
    """Небольшой контейнер с последней записью."""

    filename: Path
    duration: float


class AudioRecorder:
    """Инкапсуляция записи через sounddevice."""

    def __init__(self) -> None:
        self._queue: queue.Queue[np.ndarray] = queue.Queue()
        self._stream: Optional[sd.InputStream] = None
        self._frames: list[np.ndarray] = []

    def start(self) -> None:
        if self._stream:
            return
        self._frames.clear()
        self._stream = sd.InputStream(
            samplerate=SAMPLE_RATE,
            channels=CHANNELS,
            dtype="float32",
            callback=self._callback,
        )
        self._stream.start()

    def stop(self) -> np.ndarray:
        if not self._stream:
            raise RuntimeError("Запись не запущена")
        self._stream.stop()
        self._stream.close()
        self._stream = None
        while not self._queue.empty():
            self._frames.append(self._queue.get())
        if not self._frames:
            raise RuntimeError("Нет данных для записи")
        return np.concatenate(self._frames, axis=0)

    def save_wav(self, data: np.ndarray, filename: Path) -> Recording:
        filename.parent.mkdir(parents=True, exist_ok=True)
        scaled = np.int16(data * 32767)
        with wave.open(str(filename), "wb") as wav:
            wav.setnchannels(CHANNELS)
            wav.setsampwidth(2)
            wav.setframerate(SAMPLE_RATE)
            wav.writeframes(scaled.tobytes())
        duration = len(data) / SAMPLE_RATE
        return Recording(filename=filename, duration=duration)

    def _callback(self, indata, frames, time, status) -> None:  
        if status:
            print("Статус записи:", status)
        self._queue.put(indata.copy())


class NeuralTranscriber:
    #"""Тонкая обертка над vosk для оффлайн-распознавания."""

    def __init__(self, model_path: Optional[str] = None):
        if not _VOSK_AVAILABLE:
            raise RuntimeError("Библиотека vosk не установлена")
        model_dir = Path(model_path or os.getenv("VOSK_MODEL_PATH", "")).expanduser()
        if not model_dir.exists():
            raise FileNotFoundError(
                "Модель vosk не найдена. Укажите путь в переменной "
                "окружения VOSK_MODEL_PATH или передайте при инициализации."
            )
        self._model = Model(str(model_dir))

    def transcribe(self, wav_path: Path) -> str:
        recognizer = KaldiRecognizer(self._model, SAMPLE_RATE)
        recognizer.SetWords(True)
        with wave.open(str(wav_path), "rb") as wf:
            while True:
                data = wf.readframes(4_000)
                if len(data) == 0:
                    break
                recognizer.AcceptWaveform(data)
        result = recognizer.FinalResult()
        return result


class DictaphoneApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("ИИ-диктофон")
        self.root.geometry("420x320")
        self.recorder = AudioRecorder()
        self.current_recording: Optional[Recording] = None
        self._transcriber: Optional[NeuralTranscriber] = None
        pygame.mixer.init(frequency=SAMPLE_RATE)

        self._build_ui()

    def _build_ui(self) -> None:
        self.status_var = tk.StringVar(value="Готов к записи")
        self.transcription_text = tk.Text(self.root, height=6)
        main = ttk.Frame(self.root, padding=12)
        main.pack(fill=tk.BOTH, expand=True)

        status_label = ttk.Label(main, textvariable=self.status_var)
        status_label.pack(fill=tk.X, pady=4)

        button_frame = ttk.Frame(main)
        button_frame.pack(pady=10)

        self.btn_start = ttk.Button(button_frame, text="Запись", command=self.start_recording)
        self.btn_stop = ttk.Button(button_frame, text="Стоп", command=self.stop_recording, state=tk.DISABLED)
        self.btn_play = ttk.Button(button_frame, text="▶ Воспроизвести", command=self.play_latest, state=tk.DISABLED)
        self.btn_save_as = ttk.Button(button_frame, text="💾 Сохранить как...", command=self.save_as, state=tk.DISABLED)
        self.btn_transcribe = ttk.Button(button_frame, text="🧠 Распознать", command=self.transcribe, state=tk.DISABLED)

        for idx, btn in enumerate(
            (self.btn_start, self.btn_stop, self.btn_play, self.btn_save_as, self.btn_transcribe)
        ):
            btn.grid(row=0, column=idx, padx=3)

        ttk.Label(main, text="Расшифровка (vosk):").pack(anchor="w")
        self.transcription_text.pack(fill=tk.BOTH, expand=True)

    def start_recording(self) -> None:
        try:
            self.recorder.start()
        except Exception as exc:
            messagebox.showerror("Ошибка", str(exc))
            return
        self.status_var.set("Запись идет...")
        self.btn_start.config(state=tk.DISABLED)
        self.btn_stop.config(state=tk.NORMAL)

    def stop_recording(self) -> None:
        try:
            data = self.recorder.stop()
        except Exception as exc:
            messagebox.showerror("Ошибка", str(exc))
            return
        filename = RECORDINGS_DIR / f"record_{_dt.datetime.now().strftime('%Y%m%d_%H%M%S')}.wav"
        try:
            self.current_recording = self.recorder.save_wav(data, filename)
        except Exception as exc:
            messagebox.showerror("Ошибка сохранения", str(exc))
            return
        self.status_var.set(f"Запись сохранена: {filename.name} ({self.current_recording.duration:.1f} c)")
        self.btn_start.config(state=tk.NORMAL)
        self.btn_stop.config(state=tk.DISABLED)
        self.btn_play.config(state=tk.NORMAL)
        self.btn_save_as.config(state=tk.NORMAL)
        self.btn_transcribe.config(state=tk.NORMAL if _VOSK_AVAILABLE else tk.DISABLED)

    def play_latest(self) -> None:
        if not self.current_recording:
            return
        try:
            pygame.mixer.music.load(str(self.current_recording.filename))
            pygame.mixer.music.play()
            self.status_var.set("Воспроизведение...")
        except Exception as exc:
            messagebox.showerror("Ошибка воспроизведения", str(exc))

    def save_as(self) -> None:
        if not self.current_recording:
            return
        path = filedialog.asksaveasfilename(
            defaultextension=".wav",
            filetypes=[("Wave files", "*.wav")],
            initialfile=self.current_recording.filename.name,
        )
        if not path:
            return
        try:
            target = Path(path)
            target.write_bytes(self.current_recording.filename.read_bytes())
            self.status_var.set(f"Сохранено как {target.name}")
        except Exception as exc:
            messagebox.showerror("Ошибка сохранения", str(exc))

    def transcribe(self) -> None:
        if not _VOSK_AVAILABLE:
            messagebox.showinfo("Vosk недоступен", "Установите vosk и модель для распознавания.")
            return
        if not self.current_recording:
            return

        def worker():
            self.status_var.set("Распознавание...")
            try:
                if not self._transcriber:
                    self._transcriber = NeuralTranscriber()
                result_json = self._transcriber.transcribe(self.current_recording.filename)
                self._update_transcription(result_json)
                self.status_var.set("Распознавание завершено")
            except Exception as exc:
                messagebox.showerror("Ошибка распознавания", str(exc))
                self.status_var.set("Ошибка при распознавании")

        threading.Thread(target=worker, daemon=True).start()

    def _update_transcription(self, text: str) -> None:
        self.transcription_text.delete("1.0", tk.END)
        self.transcription_text.insert(tk.END, text)


def main() -> None:
    root = tk.Tk()
    DictaphoneApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()

