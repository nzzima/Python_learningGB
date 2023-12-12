# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
import json

telephone_book = {}

while True:
    command = input("Enter command: ")
    if command == "Add":
        name = input("Enter name: ")
        phone = input(f"Enter {name}'s phone: ")
        answear_more = input(f"Do you want to add email and birthday date for  {name} (y/n) ? --> ")
        if answear_more.lower() == "yes" or answear_more.lower == "y":
            email = input("Enter email with '@' : ")
            birthday = input("Enter birthday date: ")
            contact_info = {'phones': [phone], 'birthday': birthday, 'email': email}
            telephone_book[name] = contact_info
            print("SUCCESS ADD")
        elif answear_more.lower() == "no" or answear_more.lower() == "n":
            contact_info = {'phones': [phone]}
            telephone_book[name] = contact_info
            print("SUCCESS ADD")

    elif command == "Show":
        for name, values in telephone_book.items():
            print(name, values)
    
    elif command == "Save":
        with open("Phone_book.json", "w", encoding="utf-8") as file:
            json.dump(telephone_book, file)
        print("SUCCESS SAVE")
    
    elif command == "Take":
        with open("Phone_book.json", "r", encoding="utf-8") as file:
            info_json = file.read()
            telephone_book = json.loads(info_json)
            # print("Took dict: ", telephone_book)
    elif command == "Search":
        print("What you would like to search?\n[Name, phones, email, birthday]")
        user_would_like = input("Enter --> ")
        

    elif command == "Exit":
        exit()
        
