from logger import input_data, print_data, edit_record

def interface():
    print("Добрый день, вы попали на специальный бот справочник \n 1 - запись данных \n 2 - Вывод данных \n 3 - Удаление данных")
    command = int(input('Введите число '))

    
    
# interface()
    if command == 1:
        input_data()
    elif command ==2:
        print_data()
    # elif command == 3:
        # remove_data()
    elif command == 4:
        edit_record()
