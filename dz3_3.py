import random

def get_uniq_word(word_list, repeat_list):
    try_count = len(word_list);
    while True:
        if try_count <= 0:
            uniq_word = None
            break

        uniq_word = random.choice(word_list)
        if uniq_word in repeat_list:
            try_count -= 1
            continue

        break

    return uniq_word

def get_jokes(joke_num, repeat=True):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

    jokes = []          # Список шуток на основе случайной генерации слов
    repeat_list = []    # Список используемых слов для избежания повторов

    while joke_num > 0:

        nouns_rand_word = get_uniq_word(nouns, repeat_list)
        if nouns_rand_word == None:
            break
        repeat_list.append(nouns_rand_word)

        adverbs_rand_word = get_uniq_word(adverbs, repeat_list)
        if adverbs_rand_word == None:
            break
        repeat_list.append(adverbs_rand_word)

        adjectives_rand_word = get_uniq_word(adjectives, repeat_list)
        if adjectives_rand_word == None:
            break
        repeat_list.append(adjectives_rand_word)

        jokes.append(f'{nouns_rand_word} {adverbs_rand_word} {adjectives_rand_word}')
        joke_num -= 1

    return jokes

print(get_jokes(20))