import sys

if len(sys.argv) <= 1:
    print('Введите сумму для записи')
    exit(1)

input_sum = float(sys.argv[1].replace(',', '.'))

with open('bakery.csv', 'a', encoding='utf-8') as file_write:
    file_write.write(f'{input_sum}\n')

print('Данные добавлены')