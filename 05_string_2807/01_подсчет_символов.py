phrase = input('Введите фразу: ')

length = 0
for symbol in phrase:  # перебираются символы строки
    length += 1

print('Длина строки "', phrase, '" - ', length)
