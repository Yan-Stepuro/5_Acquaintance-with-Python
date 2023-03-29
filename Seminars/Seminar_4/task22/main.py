# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во элементов второго множества. 
# Затем пользователь вводит сами элементы множеств.

n = int(input('Введите размер 1го множества: '))
m = int(input('Введите размер 2го множества: '))

list_n = []
list_m = []

for i in range(n):
    list_n.append(int(input('Введите {} число 1 множества: '.format(i))))

for i in range(m):
    list_m.append(int(input('Введите {} число 2 множества: '.format(i))))

print(list_n)
print(list_m)

set_n = set()
set_m = set()

set_n = set(list_n)
set_m = set(list_m)

print(set_n)
print(set_m)

set_u = set_n.union(set_m)
print(set_u)

list_u = list(set_u)
print(list_u)

list_u.sort()

print(list_u)
