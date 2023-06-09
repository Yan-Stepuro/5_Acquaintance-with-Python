# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

# *Пример:*
# 3 2 4 -> yes
# 3 2 1 -> no

# k должно быть кратно либо m либо n 

m = int(input('Введите длину шоколадки: '))
n = int(input('Введите ширину шоколадки: '))
k = int(input('Сколько долек хотите отломить: '))

# m > 0
# n > 0
# k > 0
# k < m * n

if m <= 0 or n <= 0 or k <= 0:
    print('Значения должны быть больше 0')
elif k < m * n and (k % m == 0 or k % n == 0):
    print(f'От шоколадки размером {m}x{n} можно отломить {k} долек')
else:
    print(f'От шоколадки размером {m}x{n} нельзя отломить {k} долек')


