# -*- coding: utf-8 -*-
import requests
from datetime import datetime
import sys
import ollama

sys.stdout.reconfigure(encoding='utf-8')

cities = {
    "Баткенская область": ["Баткен", "Кызыл-Кыя", "Сульукта"],
    "Ошская область": ["Ош", "Узген", "Ноокат", "Кара-Суу"],
    "Джалал-Абадская область": ["Джалал-Абад", "Кара-Куль", "Майлуу-Суу", "Таш-Кумыр", "Кочкор-Ата"],
    "Таласская область": ["Талас", "Кара-Буура", "Манас"],
    "Нарынская область": ["Нарын", "Ат-Баши", "Чаек"],
    "Иссык-Кульская область": ["Каракол", "Чолпон-Ата", "Балыкчы", "Тамга", "Боконбаево"],
    "Чуйская область": ["Токмок", "Кара-Балта", "Кант", "Шопоков", "Каинды"],
    "Бишкек": ["Бишкек"]
}
all_cities = [c for cities_list in cities.values() for c in cities_list]
history = []
ai_model = None

def get_time():
    now = datetime.now()
    days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
    return f"Сегодня {days[now.weekday()]}, {now.strftime('%d.%m.%Y')}, время: {now.strftime('%H:%M:%S')}"

def get_weather(city):
    try:
        data = requests.get(f"https://wttr.in/{city}?format=j1&lang=ru", timeout=10).json()
        curr = data["current_condition"][0]
        today = data["weather"][0]
        return (f"🌤️ Погода в {city}:\n"
                f"   Температура: {curr['temp_C']}°C (ощущается {curr['FeelsLikeC']}°C)\n"
                f"   Условия: {curr['weatherDesc'][0]['value'].lower()}\n"
                f"   Влажность: {curr['humidity']}% | Ветер: {curr['windspeedKmph']} км/ч\n"
                f"   Сегодня: от {today['mintempC']}°C до {today['maxtempC']}°C")
    except Exception as e:
        return f"❌ Ошибка получения погоды: {e}"

def setup_ai():
    global ai_model
    try:
        models = ollama.list()
        model_list = models.get('models', []) if isinstance(models, dict) else models
        for m in model_list:
            name = m.get('name', '') if isinstance(m, dict) else str(m)
            if name:
                ai_model = name.split(':')[0]
                return True
    except Exception:
        pass
    return False

def ask_ai(text):
    global history, ai_model
    if not ai_model:
        return "❌ AI недоступен. Установите модель: ollama pull llama3.2"
    try:
        messages = [{"role": "system", "content": "Ты дружелюбный AI-помощник. Отвечай вежливо."}]
        if history:
            messages.extend(history[-10:])
        messages.append({"role": "user", "content": text})
        response = ollama.chat(model=ai_model, messages=messages)["message"]["content"]
        history.extend([{"role": "user", "content": text}, {"role": "assistant", "content": response}])
        if len(history) > 10:
            history = history[-10:]
        return response
    except Exception:
        return "❌ Ошибка AI. Проверьте Ollama сервис."

def process_input(user_input):
    text = user_input.lower()
    if any(x in text for x in ["выход", "пока", "exit"]):
        return "exit", None
    if any(x in text for x in ["время", "который час"]):
        return "time", None
    if any(x in text for x in ["город", "города", "област"]):
        city = next((c for c in all_cities if c.lower() in text), None)
        if city and any(x in text for x in ["температур", "погод"]):
            return "weather", city
        return "cities", None
    if any(x in text for x in ["температур", "погод"]):
        city = next((c for c in all_cities if c.lower() in text), None)
        return ("weather", city) if city else ("weather_ask", None)
    return "chat", None

def main():
    print("🤖 Привет! Я ИИ помощник.")
    print("Могу помочь: время, погода в городах Кыргызстана, диалог.")
    print("Введите 'выход' для выхода.\n" + "-" * 50)
    
    if setup_ai():
        print("✅ AI готов к работе!")
    else:
        print("⚠️ AI недоступен. Работают: время, погода, города.")
    
    while True:
        try:
            user_input = input("\n👤 Ты: ").strip()
            if not user_input:
                continue
            
            cmd, param = process_input(user_input)
            
            if cmd == "exit":
                print("🤖 До встречи 👋")
                break
            elif cmd == "time":
                print(f"🕒 {get_time()}")
            elif cmd == "cities":
                print("🏙️ Города Кыргызстана:")
                for oblast, city_list in cities.items():
                    print(f"   {oblast}: {', '.join(city_list)}")
            elif cmd == "weather":
                print(get_weather(param))
            elif cmd == "weather_ask":
                if ai_model:
                    print(f"🤖 {ask_ai(f'Пользователь спрашивает про погоду. Доступные города: {', '.join(set(all_cities))}. Предложи указать город.')}")
                else:
                    print(f"❗ Укажи город: {', '.join(set(all_cities))}")
            else:
                if ai_model:
                    print(f"🤖 {ask_ai(user_input)}")
                else:
                    print("❌ AI недоступен. Доступны: время, погода, города.")
        except KeyboardInterrupt:
            print("\n\n🤖 До встречи 👋")
            break
        except Exception as e:
            print(f"❌ Ошибка: {e}")

if __name__ == "__main__":
    main()
