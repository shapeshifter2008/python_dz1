numbers = []

for num in range(1, 1001, 2):
    cube = num ** 3
    sum_numbers = 0

    cube_check = cube
    while (cube_check != 0):
        sum_numbers += cube_check % 10
        cube_check = cube_check // 10

    if (sum_numbers//7):
        cube_extra = cube + 17
        sum_numbers = 0

        cube_check = cube_extra
        while (cube_check != 0): # Можно убрать в функцию
            sum_numbers += cube_check % 10
            cube_check = cube_check // 10

        if (sum_numbers // 7):
            numbers.append(cube) # Записываем исхожное число из range возведенное в куб

print(numbers)

