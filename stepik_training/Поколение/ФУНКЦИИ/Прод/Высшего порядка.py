# # Высшего порядка - функции которые принимают и\или возвращают другие функции
# #
# # def high_order_function(func):     # функция высшего порядка, так как принимает функцию
# #     return func(3)
# #
# #
# # def double(x):                     # обычная функция = функция первого порядка
# #     return 2*x
# #
# #
# # def add_one(x):                    # обычная функция = функция первого порядка
# #     return x + 1
# #
# #
# #
# #
# # Пример использования map
# #
# # def map(function, items):
# #     result = []
# #     for item in items:
# #         new_item = function(item)
# #         result.append(new_item)
# #
# #     return result
# #
#
#
# # map принимает в себя функцию для преобразования первым аргументом
# # а вторым аргументом то, что будем преобразовывать
#
# # def square(x):
# #     return x**2
# #
# #
# # def cube(x):
# #     return x**3
# #
# #
# # numbers = [1, 2, -3, 4, -5, 6, -9, 0]
# #
# # strings = map(str, numbers)        # используем в качестве преобразователя - функцию str
# # abs_numbers = map(abs, numbers)    # используем в качестве преобразователя - функцию abs
# #
# # squares = map(square, numbers)     # используем в качестве преобразователя - функцию square
# # cubes = map(cube, numbers)         # используем в качестве преобразователя - функцию cube
# #
# # print(strings)
# # print(abs_numbers)
# # print(squares)
# # print(cubes)
# #
# #
# #
#
# Можно использовать цепочки преобразования
#
# numbers = ['-1', '20', '3', '-94', '65', '6', '-970', '8']
#
# new_numbers = map(abs, map(int, numbers))
#
# print(new_numbers)
#
# Сначала преобразование в инт,  потом из инт получаем абс
#
#
#
# Функция filter() используется для отбора элементов по критерию
#
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)  # добавляем элемент item если функция function вернула значение True
#
#     return result
#
# Если айтем будет тру, то он попадет в список резалт
#
#
# def is_greater10(num):  # функция возвращает значение True если число больше 10 и False в противном случае
#     return num > 10
#
#
# numbers = [12, 2, -30, 48, 51, -60, 19, 10, 13]
#
# large_numbers = filter(is_greater10, numbers)  #  список large_numbers содержит элементы, большие 10
#
# print(large_numbers)
#
# [12, 48, 51, 19, 13]
#
#
# Функция reduce()
#
# def reduce(operation, items, initial_value):
#     acc = initial_value
#     for item in items:
#         acc = operation(acc, item)
#
#     return acc
#
# operation - функция, которая будет умножать или складывать
# items - элементы, с которыми будем это делать
# initial_value - отправная точка, от которой это будет ( 0 или 1)
#
# def add(x, y):
#     return x+y
#
#
# def mult(x, y):
#     return x*y
#
#
# numbers = [1, 2, 3, 4, 5]
#
# total = reduce(add, numbers, 0)
# product = reduce(mult, numbers, 1)
#
# print(total)
# print(product)
#
# 15 от нуля прибавим все значения списка и вернет результат
# 120 от 1 умножим все значения спика и вернет результат




