import sys
import os
import json
# Акимкин Максим

# 1. Прочитать содержимое tests.json.
# 2. Прочитать содержимое values.json.
# 3. Обновить структуру из tests.json на основе данных из values.json.
# 4. Записать обновленную структуру в файл report.json.

# Функция для чтения JSON из файла
def read_json_data(file_path):
    with open(file_path, 'r') as f: # Открываем файл на чтение.
        return json.load(f) # Преобразуем содержимое файла в структуру данных Python и возвращаем её.

# Функция для записи JSON в файл
def write_json_data(file_path):
    with open(file_path, 'w') as f: # Открываем файл на запись.
        json.dump(tests_data, f, ensure_ascii=False, indent=1) # Записывам данные JSON в файл.

# Рекурсивная функция для обновления значений в структуре тестов
def update_values(test_structure, values_dict):
    # Если текущий элемент — словарь
    if isinstance(test_structure, dict):
        # Если у текущего словаря есть ключ 'id', и этот ID присутствует в словаре значений
        if 'id' in test_structure and test_structure['id'] in values_dict:
            # Если есть, обновляем значение для текущего элемента.
            test_structure['value'] = values_dict[test_structure['id']]
        
        # Продолжаем рекурсивный обход для всех значений словаря
        for key in test_structure:
            update_values(test_structure[key], values_dict)
    
    # Если текущий элемент — список
    elif isinstance(test_structure, list):
        # Продолжаем рекурсивный обход для каждого элемента списка
        for item in test_structure:
            update_values(item, values_dict)

# Основное тело программы
if __name__ == "__main__":
    # Проверяем, что передано два аргумента (помимо имени скрипта)
    if len(sys.argv) != 3:
        print("Необходимо передать два файла: файл tests.json и файл values.json!")
        sys.exit(1)

    # Определение файлов на основе имени или порядка передачи
    if "tests.json" in sys.argv:
        tests_file = "tests.json"
        values_file = [f for f in sys.argv[1:] if f != "tests.json"][0]
    elif "values.json" in sys.argv:
        values_file = "values.json"
        tests_file = [f for f in sys.argv[1:] if f != "values.json"][0]
    else:
        tests_file, values_file = sys.argv[1], sys.argv[2]
        
    # Проверка наличия файлов
    if not os.path.exists(tests_file) or not os.path.exists(values_file):
        print("Как минимум один из файлов не существует!")
        sys.exit(1)
    
    # Пытаемся прочитать данные из файлов
    try:
        tests_data = read_json_data(tests_file)
        values = read_json_data(values_file)
    except json.JSONDecodeError:
        print("Ошибка в формате данных файлов!")
        sys.exit(1)

    # Создаем словарь для быстрого доступа к значениям тестов
    values_dict = {item['id']: item['value'] for item in values['values']}

    # Обновляем структуру тестов с новыми значениями.
    update_values(tests_data, values_dict)
    
    # Записываем результат в файл report.json
    write_json_data('report.json') # Тут можно прописать путь

    print("Отчет сохранен в файле report.json")