# Fraction используется для работы с рациональными числами
# Чтобы его использовать, нужно подключить модуль :
from fractions import Fraction

# Создать Fraction можно несколькими способами
# 1) Из целых чисел, передач значение числителя и знаменателя дроби
# 2) из строки на основании десятичного представления
# 3) из строки на основани обыкновенной дроби
# 4)из числа с плавающей точкой (не рекомендуется)

from fractions import Fraction

num1 = Fraction(3, 4)     # 3 - числитель, 4 - знаменатель
num2 = Fraction('0.55')
num3 = Fraction('1/9')

print(num1, num2, num3, sep='\n')

# 3/4
# 11/20
# 1/9


# При создании рационального числа Fraction, автоматически происходит сокращение дроби
from fractions import Fraction

num1 = Fraction(5, 10)
num2 = Fraction('75/100')
num3 = Fraction('0.25')

print(num1, num2, num3, sep='\n')

# 1/2
# 3/4
# 1/4


# А так же происходит вывод целого числа, если указаны дроби целого числа

from fractions import Fraction

num1 = Fraction(5, 1)        # 5/1 = 5
num2 = Fraction(23, 23)      # 23/23 = 1

print(num1, num2, sep='\n')

# 5
# 1


# Fraction можно сравнивать с собой точно так же, как и любые другие числа
# Так же можно сравнивать с целыми числами и с числами с плавающей точкой без приведения типов


from fractions import Fraction

num1 = Fraction(1, 2)        # 1/2
num2 = Fraction(15, 30)      # 15/30=1/2
num3 = Fraction(3, 5)        # 3/5
num4 = Fraction(5, 3)        # 5/3
num5 = 1
num6 = 0.8


print(num1 == num2)
print(num1 != num4)
print(num2 > num3)
print(num4 <= num1)
print(num1 < num5)
print(num6 > num4)

# True
# True
# False
# False
# True
# False


# Fraction имеет все привычные арифметические операции
# Так же можно совершать операции с целыми числами без приведения типов

from fractions import Fraction

num1 = Fraction('1/10')
num2 = Fraction('2/3')

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)


# Fraction можно передавать как аргументы функций, ожидающих float
# В моудль math например. Но надо помнить, что результат будет отдан float

from fractions import Fraction
from math import *

num1 = Fraction('1.44')
num2 = Fraction('0.523')

print(sqrt(num1))
print(sin(num2))
print(log(num1 + num2))


# Свойства numerator и denominator
# Для получения числителя и знаменателя :

from fractions import Fraction

num = Fraction('5/16')

print('Числитель дроби равен:', num.numerator)
print('Знаменатель дроби равен:', num.denominator)

# Числитель дроби равен: 5
# Знаменатель дроби равен: 16

# метод as_integer_ratio()
# Возвращает кортеж, состоящий из числителя и знаменателя данного Fraction числа.
from fractions import Fraction

num = Fraction('-5/16')

print(num.as_integer_ratio())

# (-5, 16)


# Метод limit_denominator() возвращает самую близкую к данному числу рациональную дробь
# ей знаменатель не превосходит переданного аргумента.

from fractions import Fraction
import math

print('PI =', math.pi)

num = Fraction(str(math.pi))

print('No limit =', num)

for d in [1, 5,  50, 90, 100, 500, 1000000]:
    limited = num.limit_denominator(d)
    print(limited)

# PI = 3.141592653589793
# No limit = 3141592653589793/1000000000000000
# 3
# 16/5
# 22/7
# 267/85
# 311/99
# 355/113
# 3126535/995207

# В Python нельзя совершать арифметические операции (+, -, *, /) между типами Decimal и Fraction
















