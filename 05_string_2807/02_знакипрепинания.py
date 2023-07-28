phrase = input('Введите фразу: ')

punct = 0
for symbol in phrase:  # проходимся по каждому из символов в строке
    if symbol == '.':  # сравниваем символы со знаками препинания
        punct += 1
    elif symbol == ',':
        punct += 1
    elif symbol == '!':
        punct += 1
    elif symbol == '?':
        punct += 1

print('количество знаков препинания: ', punct)
