import os
import json

scan_dir = './my_project'
size_limits = [100, 1000, 10000, 100000]
size_limits.sort(reverse=False) # Сортируем на случай, если значения массива будут не по порядку
logs = {}

for root, dirs, files in os.walk(scan_dir):
    for file in files:
        file_size = os.stat(f'{root}/{file}').st_size
        file_extension = os.path.basename(f'{root}/{file}').split('.').pop()
        in_limit = False

        for limit in size_limits:
            if file_size < limit:
                in_limit = True
                tmp_data = logs.get(limit, {'num': 0, 'ext': []})
                tmp_data['num'] += 1
                if file_extension not in tmp_data['ext']:
                    tmp_data['ext'].append(file_extension)

                logs.update({limit: tmp_data})
                break

        # Если размер файла больше всех лимитов
        if in_limit == False:
            tmp_data = logs.get('more', {'num': 0, 'ext': []})
            tmp_data['num'] += 1
            if file_extension not in tmp_data['ext']:
                tmp_data['ext'].append(file_extension)

            logs.update({'more': tmp_data})

# Создаем кортежи по условиям ТЗ
for key, value in logs.items():
    logs.update({key: (value['num'], value['ext'])})

with open(f'{os.path.basename(scan_dir)}_summary.json', 'w', encoding='utf-8') as file_out:
    json.dump(logs, file_out, ensure_ascii=False)