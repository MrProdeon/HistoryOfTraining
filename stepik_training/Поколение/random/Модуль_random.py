# # Модуль random
#
# # Для подключения модуля необходимо прописать :
#
# import random
#
# # После подключения модуля, мы можем использовать его функции
#
# # Функция randint()
#
# # Функция принимает два обязательные аргумента и возвращает случайное число из их отрезка
#
#
# import random
#
# num1 = random.randint(0, 17)
# num2 = random.randint(-5, 5)
#
# print(num1)  # Выведет рандомное число от 0 до 17
# print(num2)  # Выведет рандомное число от -5 до 5
#
# # ВАЖНО
# # Левая и правая граница ВКЛЮЧИТЕЛЬНЫ
#
# import random
#
# for _ in range(10):
#     print(random.randint(1, 100))
#
# # Данный код выведет 10 случайных чисел в диапазоне от 1 до 100
# # Среди этих чисел могут быть повторени , т.к. каждый раз выбирается рандомное число
#
#
# # Функция randrange()
#
# import random
#
# num = random.randrange(10)
#
# # Данная функция вернет рандомное число в переменную от 0 до 9, то есть до 10 невключительно
#
# num = random.randrange(5, 10)
#
# # Вернет рандомное число в num от 0 до 9(вкл) до 10 невкл
#
# num = random.randrange(0, 101, 10)
#
# # 1 число начало, 2 число конец невкл, 3 число шаг
# # Вернет рандомное число из 0, 10, 20 ....
#
#
# # Функция random()
#
# # Вернет случайное число с плавающей точкой в диапазоне от 0.0 до 1.0 (невключительно)
#
# import random
#
# num = random.random()
# print(num)  # Вернет что-то от 0.0 до 1.0
#
#
# # Функция uniform()
#
# # Так же вернет число с плавающей точкой, но в качестве аргумента можно передать диапазон
#
# import random
#
# num = random.uniform(1.5, 17.3)
# print(num)  # Вернет рандом число от 1.5 до 17.3 невкл
#
# # Можно прописать импорт вот так и не писать название модуля через точку каждый раз
# from random import *
#
# num = randint(1, 100)
#
#
# # Функция shuffle()
#
# # Принимает список в качестве аргумента и перемешивает его рандомным образом
#
# import random
#
# num = [1, 2, 3, 4, 5]
# random.shuffle(num)
# print(num)  # Выведет перемешанный список
#
#
# # Функция choice()
#
# # Принимает список, кортеж или строку в качестве аргумента и вернет один случайный элемент из этого аргумента
#
# import random
#
# num = [1, 2, 3]
# s = "Python"
#
# print(random.choice(num))  # Выведет рандомное число из списка num
# print(random.choice(s))  # Выведет рандомный элемент строки s
#
#
# # Функция sample()
# # Принимает в качестве аргумента список, кортеж или строку, а так же количество элементов, которые нужно рандомно вывести
#
# import random
#
# num = [1, 2, 3]
# s = "Python"
#
# print(random.sample(num, 2))  # Выведет СПИСОК 2 числа из списка num
# print(random.sample(s, 2))  # Выведет СПИСОК 2 буквы из строки s
#
# # Если мы запрашиваем вывести больше элементов, чем содержит строка или список - выведет ошибку
#
#
# #Модуль string
# #Имеет удобные константные строки для вывода
#
# import string
#
# print(string.ascii_letters)
# print(string.ascii_uppercase)
# print(string.ascii_lowercase)
# print(string.digits)
# print(string.hexdigits)
# print(string.octdigits)
# print(string.punctuation)
# print(string.printable)
#
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# abcdefghijklmnopqrstuvwxyz
# 0123456789
# 0123456789abcdefABCDEF
# 01234567
# !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
# 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~ \t\n\r\x0b\x0c
