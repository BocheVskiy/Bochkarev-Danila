# Задача-3: Напишите программу, вычисляющую корни квадратного уравнения вида
# ax² + bx + c = 0.
# Коэффициенты уравнения вводятся пользователем.
# Для вычисления квадратного корня воспользуйтесь функцией sqrt() модуля math:
# import math
# math.sqrt(4) - вычисляет корень числа 4

# TODO: код пишем тут...

import math


print('Введите значения для данного уравнения -  ax² + bx + c = 0')
a = int(input('Введите значение a: '))
b = int(input('Введите значение b: '))
c = int(input('Введите значение c: '))

D = b**2 - 4 * a * c
print(D)

if D > 0:
    x1 = (-b + match.sqrt(D)) / (2 * a)
    x2 = (-b - match.sqrt(D)) / (2 * a)
    print(x1, x2)
elif D == 0:
    x = -b / (2 * a)
    print(x)
else:
    print('Нет корней')