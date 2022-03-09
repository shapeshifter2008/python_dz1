rand_numbers = [10.1, 98.12, 8.01, 50.0, 71.77, 8.8, 1000]
print(id(rand_numbers))
rand_numbers.sort()
print(id(rand_numbers))

for number in rand_numbers:
    rub = int(number)
    rub_k = (number-rub)*100
    print(f'{rub} руб {rub_k:02.0f} коп', end=', ')

print('')

rand_numbers_reverse = rand_numbers.copy()

for number in sorted(rand_numbers_reverse)[::-1][:5]:
    rub = int(number)
    rub_k = (number-rub)*100
    print(f'{rub} руб {rub_k:02.0f} коп', end=', ')