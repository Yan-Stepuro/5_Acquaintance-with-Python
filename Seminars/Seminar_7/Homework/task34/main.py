# Задача 34:  Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. 
# Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу. 
# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
# Стихотворение  Винни-Пух вбивает в программу с клавиатуры. В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

# *Пример:*

# **Ввод:** пара-ра-рам рам-пам-папам па-ра-па-да    
#     **Вывод:** Парам пам-пам  


# def inputValue(message):
#    return input(message).split()

value = "тра туу тыы".split()
print(value)
print(type(value))
print(value[0])
print(type(value[0]))


vowels = "ауоыиэяюёе"
print(vowels)

def countVowels(value, vowels):
    list = []
    сс = 0
    for i in value:
        for k in i:
            for j in vowels:
                if k in j:
                    сс += 1
                    list.append(сс)

    # for i in list:
    #     if len(i)
    
    return list

print(countVowels(value, vowels))

# def countVowels(vowels):
#     cc = 0
#     value = filter()
#     for i in value:
#         for j in vowels:
#             if i in j:
#                 cc += 1
#                 print(i, j, cc)
#     return cc






# word = "mytestword"
# cword = len(word)
# vowels = "aeuioy"

# i = 1
# cc = 0
# for w in word:
#   for c in vowels:
#     if c in w:
#       cc += 1

# print(cc)

