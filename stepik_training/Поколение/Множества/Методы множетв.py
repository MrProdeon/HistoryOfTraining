#1
#-add         добавить один элемент(добавит полностью всю строку)
#-remove      удаляет все элементы с генерацией ошибки
#-discard     удаляет все элементы без генерации ошибки
#-pop         удаляет случайный элемент множества, возвращая его
#-clear       удаляет все элементы множества

#2.1
#-union                          |      объединяет множества создавая новое множество     |
#-intersection                   &      пересечение множества (общие элементы)            || создавая новое
#-difference                     -      разность множеств(то, чего нет в другом элементе) || множество
#-symmetric_difference           ^      выводит множество без общих элементов             |

#2.2
#update                          |=     изменяет исходное множество по объединению                                  |
#intersection_update             &=     изменяет исходное множество по пересечению (общие элементы)                 || изменяет исходное
#difference_update               -=     изменяет исходное множество по разности(то, чего нет в другом элементе)     || множество
#symmetric_difference_update     ^=     изменяет исходное множество, выводит исходное множество без общих элементов |

myset1, myset2 = set(range(11)), set(range(5, 15))

#FIRST:
#myset1.add('gfgggfgf')
#print('add =', myset1)

#myset1.remove(15)
#print('remove =', myset1)

#myset1.discard(11)
#print('discard =', myset1)

#pop = myset1.pop()
#print('pop =', pop)  # По ощущению, будто удаляет только первый элемент, странно

#myset1.clear()
#print('clear =', myset1)


#SECOND_1:
#new_set = myset1.union(myset2)
#print('union =', new_set)

#new_set = myset1.intersection(myset2)
#print('intersection =', new_set)

#new_set = myset1.difference(myset2)
#print('defference =', new_set)

#new_set = myset1.symmetric_difference(myset2)
#print('symmetric_difference', new_set)


#SECOND_2:
#myset1.update(myset2)
#print('update', myset1)

#myset1.intersection_update(myset2)
#print('intersection_update =', myset1)

#myset1.difference_update(myset2)
#print('difference_update =', myset1)

#myset1.symmetric_difference_update(myset2)
#print('symmetric_difference_update =', myset1)



#union = |
#intersection = &
#difference = -
#symmetric_difference = ^

#update = |=
#intersection_update = &=
#difference_update = -=
#symmetric_difference_update = ^=
                                                 # Приоритеты операторов (чем выше - тем выше приоретет)
#  -
#  &
#  ^
#  |