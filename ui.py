from logger import input_data, print_data, del_data, delete2_data
def interface():
    print("Добрый день, вы попали на специальный бот справочник \n 1 - запись данных \n 2 - Вывод данных \n 3 - удаление данных из первого файла \n 4 - удаление из второго файла" )
    command = int(input('Введите число '))

    while command != 1 and command != 2 and command != 3 and command != 4: 
        print("неправильный ввод")
        var = int(input('Введите число: '))
    # interface()
    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        del_data()
    elif command == 4:
     delete2_data()