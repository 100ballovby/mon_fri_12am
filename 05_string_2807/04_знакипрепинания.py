phrase = input('Введите фразу: ')

symbols = 0
for symbol in phrase:
    if symbol in '.,!?-;:':
        symbols += 1

print('количество знаков препинания: ', symbols)
