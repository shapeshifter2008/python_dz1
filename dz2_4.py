words_list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

for word in words_list:
    word_split = word.split(' ');
    name = word_split.pop().title()
    print(f'Привет, {name}!')
