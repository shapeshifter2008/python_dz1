from itertools import zip_longest
import json

users_hobby_data = {}

with open('users.csv', 'r', encoding='utf-8') as file_users:
    with open('hobby.csv', 'r', encoding='utf-8') as file_hobby:

        if len(list(file_users)) < len(list(file_hobby)):
            exit(1)

        # Сбрасываем указатели для цикла ниже
        file_users.seek(0)
        file_hobby.seek(0)

        # zip_longest - в случае отсутствия значения бует подставлен None
        for user, hobby in zip_longest(file_users, file_hobby):
            last_name, first_name, middle_name = user.strip().split(',')

            if (hobby is None):
                hobby_line = hobby
            else:
                hobby_line = hobby.strip()

            users_hobby_data[f'{last_name} {first_name} {middle_name}'] = hobby_line

print(users_hobby_data)

with open('dz6_out.json', 'w', encoding='utf-8') as file_out:
    json.dump(users_hobby_data, file_out, ensure_ascii=False)