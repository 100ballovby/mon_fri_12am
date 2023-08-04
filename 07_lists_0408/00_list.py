lst = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f'На месте элемента с индексом 3 находится: {lst[3]}')
print(lst)
print(lst[:5])
print([10, 20, 30] + [40, 50, 60, 70])
print([1, 2, 3] * 4)

# перебор вариант 1:
for i in range(len(lst)):
    print(f'Индекс {i}: {lst[i]}')


# пребор вариант 2:
for element in lst:
    print(f'Элемент: {element}')


