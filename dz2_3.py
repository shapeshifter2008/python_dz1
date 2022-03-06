words_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
skip_index = 0

for key, word in enumerate(words_list):
    if skip_index > 0:
        skip_index -= 1
        continue

    if word.isdigit():
        words_list.pop(key)
        words_list.insert(key, '"')
        words_list.insert(key, f'{int(word):02}')
        words_list.insert(key, '"')
        skip_index = 3
    elif (word[0] == '+') and word[1:].isdigit():
        words_list.pop(key)
        words_list.insert(key, '"')
        words_list.insert(key, f'+{int(word[1:]):02}')
        words_list.insert(key, '"')
        skip_index = 3
    else:
        continue

print(' '.join(words_list))