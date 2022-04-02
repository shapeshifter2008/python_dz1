import os

project_structure = {
    'dirs': [
        './my_project',
        './my_project/settings',
        './my_project/mainapp',
        './my_project/adminapp',
        './my_project/authapp',
    ],
    'files': [
        './my_project/test.py',
        './my_project/random/test.py'
    ]
}

created_dirs = 0
created_files = 0

for dir_path in project_structure['dirs']:
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
        created_dirs += 1

print('Создано папок: ', created_dirs)

for file_path in project_structure['files']:
    try:
        my_file = open(file_path, "x")
        my_file.close()
        created_files += 1
    except FileExistsError:
        print('Файл уже существует: ', file_path)
    except FileNotFoundError:
        print('Не удалось создать файл (путь к файлу недоступен): ', file_path)
    except Exception as e:
        print('Неизвестная ошибка: ', e)

print('Создано файлов: ', created_files)