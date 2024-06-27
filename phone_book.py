"""
Создать телефонный справочник с возможностью импорта
и экспорта данных в формате .txt. Фамилия, имя, отчество,
номер телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для
поиска определенной записи (Например, имя или фамилию
человека)
4. Использование функций. Ваша программа не должна быть линейной
"""

from csv import DictReader, DictWriter
from os.path import exists #проверка на существование

class NameError(Exception):
    def __init__(self, txt):
        self.txt = txt


def get_info():
    flag = False
    while not flag:
        try:
            first_name = input('Введите имя: ')
            if len(first_name) < 2:
                raise NameError('Слишком короткое имя.')
            second_name = input('Введите фамилию: ')
            if len(second_name) < 4:
                raise NameError('Слишком короткая фамилия.')
            phone_number = input('Введите номер телефона: ')
            if len(phone_number) < 11:
                raise NameError('Слишком короткий номер телефона.')
        except NameError as err:
            print (err)
        else:
            flag = True
    return [first_name, second_name, phone_number]


def create_file(file_name):
    with open(file_name, 'w', encoding='utf-8', newline='') as data:
        f_w = DictWriter(data, fieldnames=['first_name', 'second_name', 
                                           'phone_number'])
        f_w.writeheader()


def write_file(file_name):
    res = read_file(file_name)
    user_data = get_info()
    new_obj = {'first_name': user_data[0], 'second_name': user_data[1], 
               'phone_number': user_data[2]}
    res.append(new_obj)
    standart_write(file_name, res)


def read_file(file_name):
    with open(file_name, encoding='utf-8', newline='') as data:
        f_r = DictReader(data)
        return list(f_r) # список со словарями
    

def remove_row(file_name):
    search = int(input('Введите номер строки для удаления: '))
    res = read_file(file_name)
    if search <= len(res):
        res.pop(search-1)
        standart_write(file_name, res)
    else:
        print('Введен неверный номер строки!')


def standart_write(file_name, res):
    with open(file_name, 'w', encoding='utf-8') as data:
        f_w = DictWriter(data, fieldnames=['first_name', 'second_name',
                                            'phone_number'])
        f_w.writeheader()
        f_w.writerows(res)
        
def change_data(file_name):
    search = int(input('Введите номер строки для изменения: '))
    res = read_file(file_name)
    while search - 1 > len(res):
        raise IndexError('Данной строки не существует.')
    user_data = get_info()
    new_obj = {'first_name': user_data[0], 'second_name': user_data[1], 
               'phone_number': user_data[2]}

    res[search-1] = new_obj
    standart_write(file_name, res)   
    

def copy_data(file_name):
    res = read_file(file_name)
    copy_file_name = input(
        'Введите имя файла, в который необходимо скопировать строку: ')
    if not exists(copy_file_name):
        create_file(copy_file_name)
    search = int(input('Введите номер строки для копирования: '))
    if search <= len(res):
        res_copy = res[search-1]
        standart_write(copy_file_name, [res_copy])
    else:
        print('Введен неверный номер строки!')


file_name = 'phone.csv'
def main():
    while True:
        print(
            '\nКоманды телефонной книги:'
            '\nДля записи нового пользователя введите "w".'
            '\nДля просмотра телефонной книги введите "r".'
            '\nДля удаления пользователя из списка введите "d".'
            '\nДля изменения пользователя из списка введите "t".'
            '\nДля копирования пользователя в новый файл введите "c".'
            '\nНажмите "q", если хотите завершить работу с программой.'
            )
        command = input('Введите команду: ')
        if command == 'q': #выход из программы
            break
        elif command == 'w': #запись данных
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name)
        elif command == 'r': #чтение данных
            if not exists(file_name):
                print('Файл отсутствует, создайте его.')
                continue
            print(*read_file(file_name))
        elif command == 'd': #удаление строк данных
            if not exists(file_name):
                print('Файл отсутствует, создайте его.')
                continue
        elif command == 't': #изменение строк данных
            if not exists(file_name):
                print('Файл отсутствует, создайте его.')
                continue
            change_data(file_name)
        elif command == 'c': #копирование файла
            if not exists(file_name):
                print('Файл отсутствует, создайте его.')
            copy_data(file_name)
            

main()


"""
реализовать копирование данных из файла А в файл В
написать функцию copy_data
прочитать список словарей (read_file)
и записать его в новый файл, используя функцию standart_write
дополнить функцию main
"""