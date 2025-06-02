# # Итераторы – важная концепция языка Python. Нужно помнить:
# #
# # Итераторы можно обойти циклом
# # Итераторы можно преобразовать в list() или tuple()
# # Итератор можно распаковать с помощью *
# #
# # numbers = [1, 10, -9, 8, 9, 345, -32, -89, 2]
# #
# # map_obj = map(abs, numbers)
# #
# # print(*map_obj)              # распаковываем
#
# Если нам нужны строковые методы в виде функции, то можем получить их через str
#
# pets = ['alfred', 'tabitha', 'william', 'arla']
# chars = ['x', 'y', '2', '3', 'a']
#
# uppered_pets = list(map(str.upper, pets))
# capitalized_pets = list(map(str.capitalize, pets))
# only_letters = list(filter(str.isalpha, chars))
#
# print(uppered_pets)
# print(capitalized_pets)
# print(only_letters)
#
# ['ALFRED', 'TABITHA', 'WILLIAM', 'ARLA']
# ['Alfred', 'Tabitha', 'William', 'Arla']
# ['x', 'y', 'a']