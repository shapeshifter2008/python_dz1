# ДЗ 1.1
while True:
    duration_sec = int(input('Введите кол-во секунд: '));
    if (duration_sec <= 0):
        print('Ошибка! Укажите число больше 0')
    else:
        break

text_min = '%d сек'
text_hour = '%d мин %d сек'
text_day = '%d час %d мин %d сек'
text_global = '%d дн %d час %d мин %d сек.'

result_day = duration_sec // (3600 * 24)
duration_sec = duration_sec % (3600 * 24)
result_hour = duration_sec // 3600
duration_sec %= 3600
result_min = duration_sec // 60
result_sec = duration_sec % 60

if (result_day):
    print(text_global % (result_day, result_hour, result_min, result_sec))
elif (result_hour):
    print(text_day % (result_hour, result_min, result_sec))
elif (result_min):
    print(text_hour % (result_min, result_sec))
elif (result_sec):
    print(text_min % (result_sec))
else:
    print('Ошибка рассчетов!')