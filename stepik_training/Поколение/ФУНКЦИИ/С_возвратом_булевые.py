# В пайтон можно писать функции с возвратом булевого значения

def is_even(number):
    if number % 2 == 0 :
        return True
    else:
        return False
    
number = int(input())

if  is_even(number):
    print('Число четное')
else:
    print('Число нечетное')       


# Функция для определения правильности ввода модели, если не 100,200 или 300, то функция будет тру, значит будем принтить наш текст
def is_invalid(model):
    if model != 100 and model != 200 and model != 300:
        return True
    else:
        return False
    
while is_invalid(model):
    print('Допустимыми номерами моделей являются 100, 200 и 300.')
    model = int(input())    