"""
bool(x) - пытается превратить тип данных переменной х в bool
"""

n1 = bool(input('Число: '))
n2 = bool(0)

print(n1, n2)

"""
bool(0) - False 
bool(1) - True 
bool(-8) - True
bool(90) - True

Bool - возвращает False в случае с переданным 0, переданным None или
пустой коллекцией - ('', [], {}, ())
"""

