# Переменное кол-во аргументов
#
# def my_func(*args):
#     print(type(args))
#     print(args)
#
#     my_func()
#     my_func(1, 2, 3)
#     my_func('a', 'b')
#
#
#
# Функция принимает параметр со звездочкой
# Это означает, что в значение args будет передан кортеж из всех аргументов, переданных при вызове функции
#
# Параметр со звездочкой обязательно должен быть в конце
# Так как если он будет в начале, он заберет на себя все аргументы
#
# def my_func(num, *args):
#     print(args)
#     print(num)
#
# my_func(17, 'Python', 2, 'C#')
#
# num примет в себя 17, а остальное уйдет в кортеж args
#
# Если передан параметр со звездочкой, то он может ничего не принимать
# Тогда он вернет пустой кортеж
#
# Можно использовать только один параметр со звездочкой
#
#
#
# Передача аргументов в форме списка и кортежа
#
# def my_sum(*args):
#     return sum(args)
#
# print(my_sum())
# print(my_sum(1))
# print(my_sum(1, 2))
# print(my_sum(1, 2, 3))
# print(my_sum(1, 2, 3, 4))
#
# В данную функцию будут передаваться значения, которое уйдут в кортеж
# И в этом кортеже посчитается и вернется сумма
#
# Так же можно вызывать данную функцию, передавая в неё список или кортеж
# Но надо их распаковать
#
# print(my_sum(*[1, 2, 3, 4, 5]))   #  распаковка списка
# print(my_sum(*(1, 2, 3)))         #  распаковка кортежа
#
# Так же можно их миксовать
#
# print(my_sum(1, 2, *[3, 4, 5], *(7, 8, 9), 10))
#
#
# Получение именованных аргументов в виде словаря
#
# Именованные аргументы передаются в **kwargs
#
# def my_func(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
#
#     my_func()
#     my_func(a=1, b=2)
#     my_func(name='Timur', job='Teacher')
#
# Пишется в самом конце, после последнего аргумента и после *args
#
# Функция может содержать *args and **kwargs
#
# def my_func(a, b, *args, name='Gvido', age=17, **kwargs):
#     print(a, b)
#     print(args)
#     print(name, age)
#     print(kwargs)
#
# my_func(1, 2, 3, 4, name='Timur', age=28, job='Teacher', language='Python')
# my_func(1, 2, name='Timur', age=28, job='Teacher', language='Python')
# my_func(1, 2, 3, 4, job='Teacher', language='Python')
#
#
#
# Именованные аргументы можно передавать пачков в виде словаря
# Для этого перед словарем нужно поставить **
#
#
# def my_func(**kwargs):
#     print(type(kwargs))
#     print(kwargs)
#
# info = {'name':'Timur', 'age':'28', 'job':'teacher'}
#
# my_func(**info)
#
# <class 'dict'>
# {'name': 'Timur', 'age': '28', 'job': 'teacher'}
#
#
#
#
# def print_info(name, surname, age, city, *children, **additional_info):
#     print('Имя:', name)
#     print('Фамилия:', surname)
#     print('Возраст:', age)
#     print('Город проживания:', city)
#     if len(children) > 0:
#         print('Дети:', ', '.join(children))
#     if len(additional_info) > 0:
#         print(additional_info)
#
# children = ['Бодхи Рансом Грин', 'Ноа Шэннон Грин', 'Джорни Ривер Грин']
# additional_info = {'height':163, 'job':'actress'}
#
# print_info('Меган', 'Фокс', 34, 'Ок-Ридж', *children, **additional_info)
#
# Имя: Меган
# Фамилия: Фокс
# Возраст: 34
# Город проживания: Ок-Ридж
# Дети: Бодхи Рансом Грин, Ноа Шэннон Грин, Джорни Ривер Грин
# {'height': 163, 'job': 'actress'}
#
#
# Keyword-only аргументы
#
# def make_circle(x, y, radius, *, line_width=1, fill=True):
#
#     * дает понять, что после неё нужно указывать строго именнованные аргументы
#     Перед * можно указывать позиционные или именованные, это неважно
#     Но после неё ТОЛЬКО именованные
#
#     * можно поставить в начале и тогда можно будет передавать только именованные аргументы
#     в противном случае будет ошибка
#
#     Такой разделитель можно использоваться только 1 раз
#     Нельзя применять в функциях с *args
#
#
# Верный порядок элементов
#
# позиционные аргументы,
# *args аргументы,
# **kwargs аргументы.
#
# def my_func(a, b, *args, **kwargs):
























