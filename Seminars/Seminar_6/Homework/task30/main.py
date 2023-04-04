# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

## решение через цикл


def inputValue(message):
   return int(input(message))

def fillArray(array, n):
    for i in range(1, n + 1):
        array.append(a + (i - 1) * d)
    return array

a = inputValue('Введите первый элемент прогрессии: ')
d = inputValue('Введите разность: ')
n = inputValue('Введите количество элементов прогрессии: ')

array = []
print(fillArray(array, n))
