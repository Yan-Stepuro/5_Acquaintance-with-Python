# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных

def read_file(filename): 
    with open(filename, 'r') as data:
        data_array = []
        for line in data:
            item = line.replace('\n','').split(sep = ',')
            data_array.append(item)
    return data_array

def write_file(filename, data_array):
    with open(filename, 'w') as data:
        for i in data_array:
            write_element = ','.join(i)
            data.write(f'{write_element}\n')

def add_item(filename, lastname = '', firstname = '', secondname = '', phone = ''):
    data_array = read_file(filename) 
    max_id = 0
    for i in range(1,len(data_array)):
        if max_id < int(data_array[i][0]): 
            max_id = int(data_array[i][0])
    next_id = max_id + 1
    print(next_id)
    lastname = input('Фамилия: ')
    firstname = input('Имя: ')
    secondname = input('Отчество: ')
    phone = input('Телефон: ')
    new_item = []
    new_item.append(str(next_id))
    new_item.append(lastname)
    new_item.append(firstname)
    new_item.append(secondname)
    new_item.append(phone)
    print(new_item)
    print(data_array)
    data_array.append(new_item)
    print(data_array)
    write_file(filename, data_array)

def show_all_items(filename):
    data_array = read_file(filename)
    print(data_array)
    for i in range(1,len(data_array)):
        print("ID: ", f"{data_array[i][0]:>3}", "Фамилия: ", f"{data_array[i][1]:>10}","Имя: ", f"{data_array[i][2]:>10}", "Отчество: ", f"{data_array[i][3]:>15}", "Телефон: ", data_array[i][4])

def change_item(filename):
    show_all_items(filename)
    data_array = read_file(filename)
    item = input('Введите ID, который требуется изменить: ')

    lastname = input('Фамилия: ')
    firstname = input('Имя: ')
    secondname = input('Отчество: ')
    phone = input('Телефон: ')

    for i in range(1, len(data_array)):
        if data_array[i][0] == item:
            data_array[i][1] = lastname
            data_array[i][2] = firstname
            data_array[i][3] = secondname
            data_array[i][4] = phone

    write_file(filename, data_array)
    show_all_items(filename)


def delete_item(filename):
    show_all_items(filename)
    data_array = read_file(filename)
    item = input('Введите ID, который требуется удалить: ')

    for i in range(1, len(data_array)):
        if data_array[i][0] == item:
            del data_array[i]

    write_file(filename, data_array)
    show_all_items(filename)

    
def menu():
    print('Добро пожаловать в телефонный справочник!')
    print('1 - Показать все записи')
    print('2 - Добавить запись')
    print('3 - Изменить запись')
    print('4 - Удалить запись')
    user_operation = int(input())

    if user_operation == 1:
        show_all_items(filename)
    elif user_operation == 2: 
        add_item(filename)
    elif user_operation == 3:
        change_item(filename)
    elif user_operation == 4:
        delete_item(filename)


filename = 'file.txt'
menu()
