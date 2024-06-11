from logger import input_data, print_data, del_data
def interface():
    print("Добрый день, вы попали на специальный бот справочник \n 1 - запись данных \n 2 - Вывод данных \n 3 - удаление данных" )
    command = int(input('Введите число '))

    
    # interface()
    if command == 1:
        input_data()
    elif command == 2:
        print_data()
    elif command == 3:
        del_data()