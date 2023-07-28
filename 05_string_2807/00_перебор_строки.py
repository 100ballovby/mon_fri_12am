phrase = input('Введите фразу: ')

# вариант перебора через индекс
for i in range(len(phrase)):
    print(phrase[i])

# Вариант перебора НЕ через индекс
for letter in phrase:  # отдаете каждый символ строки в цикл
    print(letter)
