num = 1
square = 1
n = int(input('Введите число: '))

while square <= n: # пока квадрат какого-нибудь числа не стал больше, чем n
    print(square)
    num += 1
    square = num * num  # num ** 2

