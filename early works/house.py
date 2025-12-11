import numpy as np
from PIL import Image, ImageDraw

# Настройка изображения
width, height = 700, 600
image = Image.new("RGB", (width, height), (135, 206, 250))  # Светло-голубой фон
draw = ImageDraw.Draw(image)

# Рисуем градиент неба
for y in range(height // 2):
    ratio = y / (height // 2)
    r = int(135 + (180 - 135) * ratio)
    g = int(206 + (220 - 206) * ratio)
    b = int(250 + (255 - 250) * ratio)
    draw.rectangle([0, y, width, y + 1], fill=(r, g, b))

# Рисуем траву с градиентом
grass_start = 400
for y in range(grass_start, height):
    ratio = (y - grass_start) / (height - grass_start)
    g = int(60 + (34 - 60) * ratio)
    draw.rectangle([0, y, width, y + 1], fill=(34, g, 34))

# Горы на горизонте
mountain_base_y = grass_start - 10
mountain_color_far = (120, 150, 170)
mountain_color_near = (140, 170, 190)
# Далекие горы
draw.polygon([(0, mountain_base_y),
              (120, 260),
              (240, mountain_base_y),
              (360, 255),
              (480, mountain_base_y),
              (0, mountain_base_y)], fill=mountain_color_far)
# Ближние горы
draw.polygon([(60, mountain_base_y),
              (200, 240),
              (320, mountain_base_y),
              (420, 245),
              (560, mountain_base_y),
              (60, mountain_base_y)], fill=mountain_color_near)

# Рисуем солнце с ореолом
sun_center_x, sun_center_y = 580, 100
sun_radius = 50
# Ореол
for i in range(3):
    r = sun_radius + i * 10
    alpha = 255 - i * 30
    draw.ellipse([sun_center_x - r, sun_center_y - r, 
                  sun_center_x + r, sun_center_y + r], 
                 fill=(255, 255, 200 - i * 20), outline=(255, 255, 200 - i * 20))
# Солнце
draw.ellipse([sun_center_x - sun_radius, sun_center_y - sun_radius, 
              sun_center_x + sun_radius, sun_center_y + sun_radius], 
             fill=(255, 255, 100))

# Рисуем облака (более пушистые)
cloud_positions = [(80, 120), (500, 180), (250, 100), (380, 140)]
for cx, cy in cloud_positions:
    # Больше слоев для пушистости
    draw.ellipse([cx, cy, cx + 50, cy + 35], fill=(255, 255, 255))
    draw.ellipse([cx + 25, cy - 15, cx + 75, cy + 25], fill=(255, 255, 255))
    draw.ellipse([cx + 50, cy, cx + 100, cy + 35], fill=(255, 255, 255))
    draw.ellipse([cx + 15, cy + 10, cx + 65, cy + 40], fill=(255, 255, 255))
    draw.ellipse([cx + 60, cy + 10, cx + 90, cy + 40], fill=(255, 255, 255))

# Птицы в небе
birds = [(200, 130), (300, 90), (450, 120)]
for bx, by in birds:
    draw.line([(bx - 12, by), (bx, by - 6), (bx + 12, by)], fill=(70, 70, 70), width=2)

# Рисуем корпус дома (основная часть) с тенью
house_x, house_y = 180, 250
house_width, house_height = 320, 220

# Тень дома
shadow_offset = 5
draw.polygon([
    (house_x + shadow_offset, house_y + house_height),
    (house_x + house_width + shadow_offset, house_y + house_height),
    (house_x + house_width + shadow_offset + 20, house_y + house_height + shadow_offset),
    (house_x + shadow_offset - 20, house_y + house_height + shadow_offset)
], fill=(20, 20, 20))

# Стены дома с градиентом
for y in range(house_y, house_y + house_height):
    ratio = (y - house_y) / house_height
    r = int(255 - 15 * ratio)
    g = int(245 - 10 * ratio)
    b = int(220 - 20 * ratio)
    draw.rectangle([house_x, y, house_x + house_width, y + 1], fill=(r, g, b))

# Рисуем крышу (треугольная) с градиентом
roof_points = [
    (house_x - 25, house_y),  # Левая точка крыши
    (house_x + house_width + 25, house_y),  # Правая точка крыши
    (house_x + house_width // 2, house_y - 120)  # Верхняя точка крыши
]
# Крыша с более насыщенным цветом
draw.polygon(roof_points, fill=(160, 82, 45))  # Коричневый
# Детали крыши (черепица)
for i in range(5):
    y_offset = i * 20
    if y_offset < 120:
        x1 = house_x - 25 + (house_width + 50) * (y_offset / 120)
        x2 = house_x + house_width + 25 - (house_width + 50) * (y_offset / 120)
        y = house_y - y_offset
        draw.line([x1, y, x2, y], fill=(120, 60, 30), width=2)

# Рисуем дверь с деталями
door_x, door_y = house_x + house_width // 2 - 35, house_y + house_height -
110
door_width, door_height = 70, 110
# Тень двери
draw.rectangle([door_x + 3, door_y + 3, door_x + door_width + 3, door_y + door_height + 3], 
               fill=(50, 30, 20))
# Дверь
draw.rectangle([door_x, door_y, door_x + door_width, door_y + door_height], 
               fill=(80, 50, 30))
# Панели двери
draw.rectangle([door_x + 5, door_y + 10, door_x + door_width - 5, door_y + door_height // 2 - 5], 
               outline=(60, 40, 25), width=2)
draw.rectangle([door_x + 5, door_y + door_height // 2 + 5, door_x + door_width - 5, door_y + door_height - 10], 
               outline=(60, 40, 25), width=2)
# Ручка двери
draw.ellipse([door_x + door_width - 18, door_y + door_height // 2 - 8, 
              door_x + door_width - 8, door_y + door_height // 2 + 8], 
             fill=(255, 200, 0))
draw.ellipse([door_x + door_width - 16, door_y + door_height // 2 - 6, 
              door_x + door_width - 10, door_y + door_height // 2 + 6], 
             fill=(255, 215, 0))

# Рисуем окна
# Левое окно
window1_x, window1_y = house_x + 50, house_y + 50
window_size = 70

# Загружаем и вставляем изображение человека в левое окно
try:
    person_img = Image.open(r'c:\Users\student\Downloads\unnamed.png')
    # Изменяем размер изображения под размер окна
    person_img = person_img.resize((window_size, window_size), Image.Resampling.LANCZOS)
    # Вставляем изображение в окно
    image.paste(person_img, (window1_x, window1_y))
except Exception as e:
    # Если не удалось загрузить изображение, используем стандартную заливку
    draw.rectangle([window1_x, window1_y, window1_x + window_size, window1_y + window_size], 
                   fill=(200, 230, 255))  # Светло-голубой

# Правое окно
window2_x = house_x + house_width - 120
draw.rectangle([window2_x, window1_y, window2_x + window_size, window1_y + window_size], 
               fill=(200, 230, 255))
# Рама правого окна
draw.rectangle([window2_x, window1_y, window2_x + window_size, window1_y + window_size], 
               outline=(139, 69, 19), width=4)
draw.line([window2_x + window_size // 2, window1_y, window2_x + window_size // 2, window1_y + window_size], 
          fill=(139, 69, 19), width=3)
draw.line([window2_x, window1_y + window_size // 2, window2_x + window_size, window1_y + window_size // 2], 
          fill=(139, 69, 19), width=3)

# Рисуем трубу с деталями
chimney_x = house_x + house_width - 80
chimney_y = house_y - 100
chimney_width = 35
# Тень трубы
draw.rectangle([chimney_x + 2, chimney_y + 2, chimney_x + chimney_width + 2, house_y + 2], 
               fill=(40, 40, 40))
# Труба
draw.rectangle([chimney_x, chimney_y, chimney_x + chimney_width, house_y], fill=(90, 90, 90))
# Верх трубы
draw.rectangle([chimney_x - 3, chimney_y, chimney_x + chimney_width + 3, chimney_y + 8], 
               fill=(70, 70, 70))

# Рисуем дорожку к дому
path_start_x = door_x + door_width // 2
path_start_y = house_y + house_height
path_width = 40
for i in range(30):
    y = path_start_y + i * 8
    width_at_y = path_width + i * 2
    x = path_start_x - width_at_y // 2
    draw.rectangle([x, y, x + width_at_y, y + 8], fill=(180, 170, 160))
    # Камни на дорожке
    if i % 3 == 0:
        stone_x = x + width_at_y // 4
        draw.ellipse([stone_x, y + 2, stone_x + 6, y + 6], fill=(150, 140, 130))


# Добавляем Мелстроя слева от аллеи на переднем плане
try:
    person_foreground = Image.open('person.png')
    person_height = 180
    w, h = person_foreground.size
    person_foreground = person_foreground.resize((int(person_height * w / h), person_height), Image.Resampling.LANCZOS)

    person_x = path_start_x - 120
    person_y = height - person_height - 20

    image.paste(person_foreground, (person_x, person_y), person_foreground.convert('RGBA'))
except Exception as e:
    print("Ошибка при вставке Мелстроя:", e)


# Загружаем второе изображение
boat = Image.open('boat.png')
# Масштабируем
boat_height = 120
w, h = boat.size
boat = boat.resize((int(boat_height * w / h), boat_height), Image.Resampling.LANCZOS)

# Координаты на синем фоне (вода)
boat_x = 550  # смещаем по горизонтали (справа)
boat_y = 280 # смещаем по вертикали (над травой / на воде)

# Вставляем с прозрачностью
image.paste(boat, (boat_x, boat_y), boat.convert('RGBA'))




# Рисуем забор
fence_y = house_y + house_height + 20
fence_height = 40
# Левая часть забора
for x in range(50, house_x - 20, 25):
    draw.rectangle([x, fence_y, x + 3, fence_y + fence_height], fill=(139, 90, 43))
    draw.polygon([(x - 5, fence_y), (x + 8, fence_y), (x + 1.5, fence_y - 8)], 
                 fill=(139, 90, 43))
# Правая часть забора
for x in range(house_x + house_width + 20, width - 50, 25):
    draw.rectangle([x, fence_y, x + 3, fence_y + fence_height], fill=(139, 90, 43))
    draw.polygon([(x - 5, fence_y), (x + 8, fence_y), (x + 1.5, fence_y - 8)], 
                 fill=(139, 90, 43))

# Рисуем цветы на траве
flower_positions = [(100, 450), (150, 480), (550, 460), (600, 490), (250, 470), (500, 450)]
for fx, fy in flower_positions:
    # Стебель
    draw.rectangle([fx, fy, fx + 2, fy + 15], fill=(34, 139, 34))
    # Лепестки
    draw.ellipse([fx - 5, fy - 5, fx + 7, fy + 7], fill=(255, 192, 203))  # Розовый
    draw.ellipse([fx - 3, fy - 7, fx + 5, fy + 5], fill=(255, 192, 203))
    draw.ellipse([fx - 3, fy - 3, fx + 5, fy + 9], fill=(255, 192, 203))
    draw.ellipse([fx - 7, fy - 3, fx + 1, fy + 9], fill=(255, 192, 203))
    # Центр цветка
    draw.ellipse([fx - 2, fy - 2, fx + 4, fy + 4], fill=(255, 255, 0))

# Рисуем дерево слева
tree_x, tree_y = 80, 380
# Ствол
draw.rectangle([tree_x, tree_y, tree_x + 25, tree_y + 60], fill=(101, 67, 33))
# Крона
for i in range(5):
    layer_y = tree_y - i * 15
    layer_size = 60 + i * 10
    draw.ellipse([tree_x - layer_size // 2 + 12, layer_y, 
                  tree_x + layer_size // 2 + 12, layer_y + 30], 
                 fill=(34, 139, 34))

# Сохраняем и показываем изображение
image.save('house_pil.png')
image.show()
