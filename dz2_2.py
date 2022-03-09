words_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
words_convert = []

for key, word in enumerate(words_list):
    if word.isdigit():
        words_convert.extend(['"', f'{int(word):02}', '"'])
    elif (word[0] == '+') and word[1:].isdigit():
        words_convert.extend(['"', f'+{int(word[1:]):02}', '"'])
    else:
        words_convert.append(word)

print(' '.join(words_convert))