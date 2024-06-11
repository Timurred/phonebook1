import csv
from data_ceate import name_data, surname_data, phone_data, address_data

def input_data():
    
    name = name_data()
    surname = surname_data()
    phone = phone_data()
    address = address_data()
    var = int(input(f"В каком формате записать данные\n\n"
    f"1 Вариант: \n"
    f"{name}\n{surname}\n{phone}\n{address} \n\n"
    f"2 Вариант: \n"
    f";{name};{surname};{phone};{address}\n"
    f"Выберите вариант: "))
    
    while var!=1 and var !=2 : 
        print("неправильный ввод")
        var = int(input('Введите число '))
    
    if var == 1:
        with open('phonedir1.csv', 'a' , encoding='utf-8') as f:
            f.write(f"\n{name}\n{surname}\n{phone}\n{address} \n\n")

    elif var == 2:
        with open('phonedir2.csv', 'a' , encoding='utf-8') as f:
           f.write(f"{name};{surname};{phone};{address}\n\n")


def print_data():
  
    print('Вывожу данные из первого файла \n')
    with open('phonedir1.csv', 'r' , encoding='utf-8') as f:
        phonedir1 = f.readlines()
        phonedir1_list = []
        j = 0
        for i in range(len(phonedir1)):
            if phonedir1[i] == '\n' or i == len(phonedir1)-1: # с помощью среза записываем новую запись от 0 до 1
                phonedir1_list.append(''.join(phonedir1[j:i+1]))
                j=i
        print(''.join(phonedir1_list))
    
    
    print('Вывожу данные из второго файла\n')
    with open('phonedir2.csv', 'r' , encoding='utf-8') as f:
        phonedir2 = f.readlines()
        print(*phonedir2)

def del_data():
    memderName = input("введите то, что нужно удалить: ")

    lines = []
    with open('phonedir1.csv', 'r' , encoding='utf-8') as readf:
        reader = csv.reader(readf)
        for row in reader:
            lines.append(row)
        lines = [row for row in lines if memderName not in row]
        with open('phonedir1.csv', 'w+' , encoding='utf-8') as writef:
            writer = csv.writer(writef)
            writer.writerows(lines)
            print(f"'{memderName}' удален")
