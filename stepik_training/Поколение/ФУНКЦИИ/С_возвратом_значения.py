# Функция с возвратом значения возвращает значение обратно в ту часть программы, которая её вызвала

# def название_функции():
# блок кода
# return выражение

# Значение выражения, которое следует за return будет отправлено в ту часть программы, которая вызвала функцию


def convert_to_celsius(temp):
    result = (5 / 9) * (temp - 32)
    return result


# Эта функция вернет результат вычисления, которое мы делали в переменной result, если эту функцию вызовут


# функция перевода градусов Фаренгейта в градусы Цельсия
def convert_to_celsius(temp):
    result = (5 / 9) * (temp - 32)
    return result


# основная программа
temp = float(input("Bвeдитe количество градусов по Фаренгейту: "))
celsius = convert_to_celsius(temp)
print(celsius)  # градусы Цельсия


# Можно уменьшить программу тем, что не создает отдельную переменную, а просто вернет результат вычислений


def convert_to_celsius(temp):
    return (5 / 9) * (temp - 32)


# Можно использовать несколько возвратом в одной функции с условным оператором if
#
#  Тут мы сразу несколько раз пишем возврат значения, если введенная оценка будет меньше какого-то значения


def convert_grade(grade):
    if grade >= 90:
        return 5
    elif grade >= 80:
        return 4
    elif grade >= 70:
        return 3
    elif grade >= 60:
        return 2
    else:
        return 1


# основная программа
grade = int(input("Введите вашу отметку по 100-балльной системе: "))
print(convert_grade(grade))


# А тут мы присваиваем значение переменной result, а потом вызываем её
def convert_grade(grade):
    if grade >= 90:
        result = 5
    elif grade >= 80:
        result = 4
    elif grade >= 70:
        result = 3
    elif grade >= 60:
        result = 2
    else:
        result = 1

    return result
