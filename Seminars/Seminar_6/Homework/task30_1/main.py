# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

## решение через рекурсию

def inputValue(message):
   return int(input(message))

def fillArray(array, n):
    if n <= 0:
        return array
    else:
        array.append(a + (n - 1) * d)
        return fillArray(array, n - 1)

a = inputValue('Введите первый элемент прогрессии: ')
d = inputValue('Введите разность: ')
n = inputValue('Введите количество элементов прогрессии: ')

array = []
print(fillArray(array, n))