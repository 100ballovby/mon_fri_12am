import time

x = 10
while True:  # БЕСКОНЕЧНЫЙ ЦИКЛ
    x -= 1
    time.sleep(1)
    # условие выхода из цикла
    if x < 0:  # условие, которое сравнивает с 0 значение переменной х
        break  # принудительный выход из цикла (окончание цикла)
    print(x)
