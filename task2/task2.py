import sys
import os
import math
# Акимкин Максим

# 1. Прочитать координаты центра окружности и её радиус из файла1.
# 2. Прочитать координаты точек из файла2.
# 3. Для каждой точки рассчитать её расстояние от центра окружности.
# 4. Определить, лежит ли точка внутри, снаружи или на окружности.
# 5. Вывести соответствующий результат в консоль.

# Функция для чтения данных об окружности из файла
def read_circle_data(file_path):
    with open(file_path, 'r') as f: # Открываем файл на чтение.
        x, y = map(float, f.readline().split())  # Считываем координаты центра окружности
        radius = float(f.readline())  # Считываем радиус окружности
    return ((x, y), radius)  # Возвращаем кортеж из кортежа координат и радиуса

# Функция для чтения координат точек из файла
def read_points(file_path):
    points = []
    with open(file_path, 'r') as f:
        for line_num, line in enumerate(f, 1):  # добавим line_num для отслеживания номера строки
            # Удаляем лишние пробельные символы на начале и конце строки
            cleaned_line = line.strip()

            # Если строка пустая или содержит только пробелы, пропускаем её
            if not cleaned_line:
                continue

            try:
                x, y = map(float, cleaned_line.split())  # Пытаемся считать и преобразовать координаты точки
            except ValueError:
                raise ValueError(f"Ошибка на строке {line_num}: Координаты точек должны быть числами типа float!")

            points.append((x, y))

    # Проверяем, что количество точек находится в допустимом диапазоне
    if not (1 <= len(points) <= 100):
        raise ValueError("Количество точек должно быть от 1 до 100!")

    return points

# Функция для определения положения точки относительно окружности
def determine_position(point, circle_center, radius):
    x, y = point
    center_x, center_y = circle_center
    # Вычисляем расстояние от точки до центра окружности
    distance = math.sqrt((x - center_x)**2 + (y - center_y)**2)
    
    # Определяем положение точки
    if math.isclose(distance, radius):  # Если расстояние равно радиусу
        return 0  # Точка на окружности
    elif distance < radius:  # Если расстояние меньше радиуса
        return 1  # Точка внутри
    else:  # Если расстояние больше радиуса
        return 2  # Точка снаружи

# Основное тело программы
if __name__ == "__main__":
    # Проверяем, что передано два аргумента (помимо имени скрипта)
    if len(sys.argv) != 3:
        print("Необходимо передать два файла: файл с данными об окружности и файл с координатами точек!")
        sys.exit(1)
    
    # Проверяем, что файлы существуют
    circle_data_file = sys.argv[1]
    points_file = sys.argv[2]

    if not os.path.exists(circle_data_file) or not os.path.exists(points_file):
        print("Как минимум один из файлов не существует!")
        sys.exit(1)
    
    # Пытаемся прочитать данные из файлов
    try:
        circle_center, radius = read_circle_data(circle_data_file) # Считываем координаты центра и радиус
        points = read_points(points_file) # Считываем точки в виде массива (СПИСКА)
    except ValueError as e:
        print("Ошибка в формате данных файлов!\n",str(e))
        sys.exit(1)
    
    # Определяем положение каждой точки и выводим результат
    for point in points:
        print(determine_position(point, circle_center, radius))

# Соответствия ответов:
# 0 - точка лежит на окружности
# 1 - точка внутри
# 2 - точка снаружи