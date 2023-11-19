# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.

# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]

# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}

# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

def print_value(dicts):
    my_list_without_spaces = []
    for i in dicts:
        for key, value in i:
            my_list_without_spaces.append(value.strip())
    
    return my_list_without_spaces
    
    
dictionary = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, 
              {"VI": "S005"}, {"VII": "S005"}, {"V":"S009"}, {"VIII":"S007"}]

print(print_value(dictionary))