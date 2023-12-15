# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. 
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной
import json

telephone_book = {}
print("\nWelcome to PHONE_BOOK console application!\n"
            "Commands:\n"
            "- Add (add new person to telephone_book)\n"
            "- Save (save new info from telephone_book to output json file)\n"
            "- Show (printing telephone_book info to console)\n"
            "- Search (find some info about person in telephone_book)\n"
            "- Delete (remove rather some info about person, rather full info about someone) (Combined Delete + Save)\n"
            "- Change (change some info about person)")

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
            print("SUCCESS ADD\n")
            
        elif answear_more.lower() == "no" or answear_more.lower() == "n":
            contact_info = {'phones': [phone]}
            telephone_book[name] = contact_info
            print("SUCCESS ADD\n")

    elif command == "Show":
        if len(telephone_book) == 0:
            print("Dictionary is empty! Try to add something or import from JSON by command 'Take'\n")
        else:
            for name, values in telephone_book.items():
                print(name, values)
            print()
    
    elif command == "Save":
        with open("C:/Users/nzzima/Desktop/Python_learningGB/sem8/Phone_book.json", "w", encoding="utf-8") as outfile:
            json.dump(telephone_book, outfile, indent=4)
        print("SUCCESS SAVE\n")
    
    elif command == "Take":
        with open("C:/Users/nzzima/Desktop/Python_learningGB/sem8/Phone_book.json", "r", encoding="utf-8") as file:
            info_json = file.read()
            telephone_book = json.loads(info_json)
            # print("Took dict: ", telephone_book)
        print("SUCCESS IMPORT\n")
            
    elif command == "Search":
        user_name = input("Enter name --> ")
        if user_name in telephone_book:
            print("What you would like to search?\n[phones, email, birthday]")
            user_would_like = input("Enter --> ")
            
            try:
                print(telephone_book[user_name][user_would_like])
            except KeyError:
                print(f"No {user_name}'s {user_would_like} info in telephone book !\n")
        else:
            print("No such person in telephone book !\n")
                    
    elif command == "Change":
        user_name = input("Enter name --> ")
        if user_name in telephone_book:
            print("What you would like to change?\n[phones, email, birthday]")
            user_would_like = input("Enter --> ")
            
            try:
                user_input = input(f"Enter new {user_would_like}: ")
                telephone_book[user_name][user_would_like] = user_input
                print(f"SUCCESS CAHNGED {user_name}'s {user_would_like}\n")
                
            except KeyError:
                print(f"Can't change {user_name}'s {user_would_like} because it's not exist !\n")
        
        else:
            print("No such person in telephone book !\n")
        
    elif command == "Delete":
        user_name = input("Enter name --> ")
        if user_name in telephone_book:
            print("What you would like to delete?\n[phones, email, birthday, full]")
            user_would_like = input("Enter --> ")
            try:
                if user_would_like != "full":
                    del telephone_book[user_name][user_would_like]
                    
                    with open("C:/Users/nzzima/Desktop/Python_learningGB/sem8/Phone_book.json", "r", encoding="utf-8") as file:
                        info_file = file.read()
                        info_json = json.loads(info_file)
                        
                    for element in info_json[user_name]:
                        if element == user_would_like:
                            info_json[user_name].pop(element)
                            break
                                        
                    with open("C:/Users/nzzima/Desktop/Python_learningGB/sem8/Phone_book.json", "w", encoding="utf-8") as outfile:
                        json.dump(info_json, outfile, indent=4)
                    print(f"SUCCESS DELETED {user_name}'s {user_would_like}\n")
                        
                elif user_would_like == "full":
                    del telephone_book[user_name]
                    
                    with open("C:/Users/nzzima/Desktop/Python_learningGB/sem8/Phone_book.json", "r", encoding="utf-8") as file:
                        info_file = file.read()
                        info_json = json.loads(info_file)
                        
                    del info_json[user_name]
                                        
                    with open("C:/Users/nzzima/Desktop/Python_learningGB/sem8/Phone_book.json", "w", encoding="utf-8") as outfile:
                        json.dump(info_json, outfile, indent=4)
                    print(f"SUCCESS DELETED {user_name}'s FULL INFO\n")
                    
            except KeyError:
                print(f"Can't delete {user_name}'s {user_would_like} because it's not exist !\n")
        else:
            print("No such person in telephone book !\n")

    elif command == "Exit":
        exit()
        
    else:
        print("This command is not existing. Try again.")