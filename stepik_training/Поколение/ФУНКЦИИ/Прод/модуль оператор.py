# Нужно обязательно импортировать
#
# Модуль operator
# Это реализованные  математические функции, благодаря им можно не писать каждый раз элементарные функции сложения и тд
from operator import *

print(add(10, 2))               # 12        Сложение
print(truediv(10, 5))           # 2.0       Деление
print(floordiv(13, 2))          # 6         Целочисленное деление
print(pow(5, 2))                # 25        Возведение в степень
print(mod(13, 2))               # 1         Деление с остатком
print(mul(10, 2))               # 20        Умножение
print(neg(-55))                 # 55        Изменение Отрицательного на положительное число
print(neg(55))                  # -55       Изменение Положительного на отрицательное число
print(sub(25, 5))               # 20        Вычитание
print(lt(5, 25))                # True      25 < 5
print(gt(25, 5))                # True      25 > 5
print(le(5, 5))                 # True      5 <= 5
print(ge(25, 25))               # True      25 >= 25
print(eq(10, 10))               # True      10 == 10
print(ne(10, 8))                # True      10 != 8

from functools import reduce


words = ['Testing ', 'shows ', 'the ', 'presence', ', ', 'not ', 'the ', 'absence ', 'of ', 'bugs']
numbers = [1, 2, -6, -4, 3, 9, 0, -6, -1]

opposite_numbers = list(map(neg, numbers)) # Меняет знаки на противоположный плюс на минус
print(opposite_numbers)
