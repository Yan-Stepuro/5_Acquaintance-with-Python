# Задача 6: Вы пользуетесь общественным транспортом? 
# Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# *Пример:*
# 385916 -> yes
# 123456 -> no

ticketNumber = int(input('Введите шестизначный номер билета: '))

if ticketNumber < 100000 or ticketNumber > 999999:
    print('Номер билета должен быть шестизначным')
elif ticketNumber // 100000 + ticketNumber // 10000 % 10 + ticketNumber // 1000 % 10 == ticketNumber // 100 % 10 + ticketNumber // 10 % 10 + ticketNumber % 10:
    print('Ура, счастливый билетик!')
else:
    print('Обычный билет')