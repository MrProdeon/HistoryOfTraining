# ===================Метод write()========================
#
# файловая_переменная.writе(строковое_значение)
#
# Для записи данных в файл - он должен быть открыт для записи ( режимы 'w', 'a', 'r+')
#
#
#
#
#
# В файле записаны данные:
# First line of the file.
# Second line of the file.
# Third line of the file.
#
# -----
# Если файл открыт в режиме 'w' :
# Его содержимое сначала полностью стирается, а уже потом в него добавляются данные
#
# with open('myfile.txt', 'w', encoding='utf-8') as file:
#     file.write('Python and beegeek forever\n')
#     file.write('We love stepik<3')
#
# В файле будет :
# Python and beegeek forever
# We love stepik
# -----
#
#
# -----
# Если файл открыт в режиме 'a' :
#
# Запись происходит в самый конец
#
# with open('myfile.txt', 'a', encoding='utf-8') as file:
#     file.write('Python and beegeek forever\n')
#     file.write('We love stepik<3')
#
# First line of the file.
# Second line of the file.
# Third line of the file.Python and beegeek forever
# We love stepik<3
# -----
#
#
#
# -----
# Если содержимое открыть в режиме 'r+' :
# Происходит частичная перезапись его содержимого
#
# with open('myfile.txt', 'r+', encoding='utf-8') as file:
#     file.write('Python and beegeek forever\n')
#     file.write('We love stepik.')
#
# Python and beegeek forever
# We love stepik. file.
# Third line of the file.
#
#
#
#
#
#
# ========================Метод writelines()===========================
# Записывает в файл содержимое целого списка
#
# philosophers = ['Джoн Локк\n', 'Дэвид Хьюм\n', 'Эдмyнд Берк\n']
#
# with open('philosophers.txt', 'w', encoding='utf-8') as file:
#     file.writelines(philosophers)
#
#
# ===================Запись в файл с помощью print()====================
# Для записи в файл необходимо передать именованный аргумент file, указывающий на открытый файл
# Функция print() автоматически переводит на новую строку
#
# with open('philosophers.txt', 'w', encoding='utf-8') as output:
#     print('Джoн Локк', file=output)
#     print('Дэвид Хьюм', file=output)
#     print('Эдмyнд Берк', file=output)
#
# Можно использовать всю мощь принта для форматирования текста файла :
#
# with open('philosophers.txt', 'w', encoding='utf-8') as output:
#     print('Джoн Локк', 'Дэвид Хьюм', 'Эдмyнд Берк', sep='***', file=output)
#
# Джoн Локк***Дэвид Хьюм***Эдмyнд Берк
#
#
