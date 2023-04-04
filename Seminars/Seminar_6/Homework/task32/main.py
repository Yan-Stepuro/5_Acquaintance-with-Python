# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)


def findIndex(array, min, max):
    valuesIndex = [i for i in range(len(array)) if array[i] >= min and array[i] <= max]
    return valuesIndex


min = int(input('Введите минимальное значение: '))
max = int(input('Введите максимальное значение: '))

import sys, random

if min >= max: 
    sys.exit('Введены некорректные значения')

array = [random.randint(0, 100) for i in range(10)]
print(array)

print(findIndex(array, min, max))



