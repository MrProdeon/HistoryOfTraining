# from functools import reduce
#
# Анонимные функции - это функции с телом, но без имени
# Пример служит однострочный оператор lambda
#
# lambda список_параметров: выражение
#
# Список параметров - список параметров через запятую
# Выражение - значение, либо код, дающий значение
#
# Параметры анонимных функций не нужно заключать в скобки, в отличие от обычных функций
#
# Стандартная функций
#
# def standart(x):
#     return x*2
#
# Анонимная функция
#
# lambda_functios = lambda x: x*2
#
# print(standard_function(7))
# print(lambda_function(7))
#
# Обе вернут 14
#
#
#
# f1 = lambda 10 + 20
# f2 = lambda x, y: x + y
# f3 = lambda x, y, z: x + y + z
#
# print(f1())
# print(f2(5,10))
# print(f3(5,10,30))
#
# 30
# 15
# 45
#
#
#
# ОДНОКРАТНОЕ ИСПОЛЬЗОВАНИЕ ФУНКЦИИ_________________
#
# points = [(1, -1), (2, 3), (-10, 15), (10, 9), (7, 18), (1, 5), (2, -4)]
#
# print(sorted(points,key=lambda point : point[1])) Сортируем по второму элементу
# print(sorted(points,key=lambda point : point[0] + point[1])) Сортируем по сумме элементов
#
#
#
# ПЕРЕДАЧА АНОНИМНЫХ ФУНКЦИЙ В КАЧЕСТВЕ АРГУМЕНТОВ ДРУГИМ ФУНКЦИЯМ_____________________________
# Анонимные функции удобно передавать в функции высшего порядка
#
# numbers = [1, 2, 3, 4, 5]
#
# new_numbers1 = list(map(lambda x : x + 1, numbers))
# new_numbers2 = list(map(lambda x : x * 2, numbers))
# new_numbers3 = list(map(lambda x : x**2, numbers))
#
# [2, 3, 4, 5, 6, 7]
# [2, 4, 6, 8, 10, 12]
# [1, 4, 9, 16, 25, 36]
#
#
#
#
# strings = ['a', 'b', 'c', 'd', 'e']
# numbers = [3, 2, 1, 4, 5]
#
# new_strings = list(map(lambda x,y : x * y, strings,numbers))
#
# ['aaa', 'bb', 'c', 'dddd', 'eeeee']
#
#
#
#
# numbers = [-1, 2, -3, 4, 0, -20, 10, 30, -40, 50, 100, 90]
#
# positive_numbers = list(filter(lambda x: x > 0, numbers))
# large_numbers = list(filter(lambda x: x > 50, numbers))
# even_numbers = list(filter(lambda x : x % 2 == 0, numbers))
#
# [2, 4, 10, 30, 50, 100, 90]
# [100, 90]
# [2, 4, 0, -20, 10, 30, -40, 50, 100, 90]
#
#
#
#
# words = ['python', 'stepik', 'beegeek', 'iq-option']
# new_words1 = list(filter(lambda x: len(x) > 6, words))
# new_word2 = list(filter(lambda x: 'e' in x, words))
#
#
# words = ['python', 'stepik', 'beegeek', 'iq-option']
# numbers = [1, 2, 3, 4, 5, 6]
#
# summa = reduce(lambda x,y : x + y, numbers, 0)
# product = reduce(
#     lambda x,y : x * y,
#     numbers,
#     1
#     )
#
#
#
# Возвращение функции в качестве результата другой функции____________________________________
# def generator_square_polynom(a, b, c):
#     return lambda x: a*x**2 + b*x + c
#
# pol = generator_square_polynom(10, 10 ,15)
# result = pol(5)
# print(result)
#
#
# Условный оператор в теле анонимной функции_______________________________
#
# значение1 if условие else значение2
#
# numbers = [-2, 0, 1, 2, 17, 4, 5, 6]
# result = list(map(lambda x: 'even' if x % 2 == 0 else 'odd', numbers))
# print(result)
#
# ['even', 'even', 'odd', 'even', 'odd', 'even', 'odd', 'even']
#
#
# Передача аргументов в анонимную функцию____________________________
#
# f1 = lambda x, y, z: x + y + z
# f2 = lambda x, y, z=3: x + y + z
# f3 = lambda *args: sum(args)
# f4 = lambda **kwargs: sum(kwargs.values())
# f5 = lambda x, *, y=0, z=0: x + y + z
#
#
# print(f1(1, 2, 3))
# print(f2(1, 2))
# print(f2(1, y=2))
# print(f3(1, 2, 3, 4, 5))
# print(f4(one=1, two=2, three=3))
# print(f5(1))
# print(f5(1, y=2, z=3))
#
# 6
# 6
# 6
# 15
# 6
# 1
# 6
#
#
#
# Особенности и ограничения анонимных функций в Python:
# анонимная функция может содержать только выражение, и не может включать в свое тело операторы;
# в теле анонимной функции такие операторы, как return, pass, assert или raise, вызовут исключение SyntaxError;
# анонимная функция пишется как одна строка исполнения;
# анонимная функция может быть немедленно вызвана


# Интересная особенность анонимных функций (лямбда-функций) – они являются выражениями.
# После определения лямбда-функции ее можно сразу же вызвать.
#
# print((lambda x,y : x + y)(5, 10))
# print(1+ (lambda x: x*5)(10) + 2)
#
# 15
# 53
#
#
# 1 2 3 4 5 6 7 8 9 10
#
# 3 5 7 9