# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  


def inputValue(message):
   return input(message).split()

value = inputValue("Введите стихотворение: ")

vowels = "ауоыиэяюёе"

def countVowels(value, vowels):
    list = []
    cc = 0
    flag = True

    for i in value:
        cc = 0
        for k in i:
            if k in vowels:
                cc += 1
        list.append(cc)
    
    # print(list)

    for i in range(0, len(list)):
            if list[0] != list[i]:
                flag = False

    if flag is True: print("Парам пам-пам")
    else: print("Пам парам")
        
    return

print(countVowels(value, vowels))

