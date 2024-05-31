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
    with open(file_name, 'w', encoding='utf-8') as data:
        f_w = DictWriter(data, fieldnames=['first_name', 'second_name',
                                           'phone_number'])
        f_w.writeheader()
        f_w.writerows(res)


def read_file(file_name):
    with open(file_name, encoding='utf-8', newline='') as data:
        f_r = DictReader(data)
        return list(f_r) # список со словарями

file_name = 'phone.csv'
def main():
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'w':
            if not exists(file_name):
                create_file(file_name)
            write_file(file_name)
        elif command == 'r':
            if not exists(file_name):
                print('Файл отсутствует, создайте его.')
                continue
            print(*read_file(file_name))
            

main()