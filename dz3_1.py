def num_translate_adv(word_eng):
    translate = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'один',
    }

    get_translate = translate.get(word_eng.lower())

    if (get_translate == None):
        return 'Ошибка!'

    if (word_eng[0:1].isupper()):
        get_translate = get_translate.title()

    return get_translate

print(num_translate_adv('One'))
print(num_translate_adv('eight'))
print(num_translate_adv('One2'))