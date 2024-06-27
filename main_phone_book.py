import commands_pb as com

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
            if not com.exists(file_name):
                com.create_file(file_name)
            com.write_file(file_name)
        elif command == 'r': #чтение данных
            if not com.exists(file_name):
                print('Файл отсутствует, создайте его.')
                continue
            print(com.read_file(file_name)) #*
        elif command == 'd': #удаление строк данных
            if not com.exists(file_name):
                print('Файл отсутствует, создайте его.')
                continue
        elif command == 't': #изменение строк данных
            if not com.exists(file_name):
                print('Файл отсутствует, создайте его.')
                continue
            com.change_data(file_name)
        elif command == 'c': #копирование файла
            if not com.exists(file_name):
                print('Файл отсутствует, создайте его.')
            com.copy_data(file_name)
            

main()