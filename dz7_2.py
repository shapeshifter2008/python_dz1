import os

try:
    with open('dz7_2_config.yaml', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if not os.path.exists(f'./{line}'):
                if '.' not in line:
                    os.mkdir(f'./{line}')
                else:
                    try:
                        my_file = open(f'./{line}', "x")
                        my_file.close()
                    except FileExistsError:
                        print('Файл уже существует: ', file_path)
                    except FileNotFoundError:
                        print('Не удалось создать файл (путь к файлу недоступен): ', file_path)
                    except Exception as e:
                        print('Неизвестная ошибка: ', e)

except FileNotFoundError as e:
    print('Файл конфигурации ./dz7_2_config.yaml не найден!', e)
    exit(1)

print('Структура проекта создана!')