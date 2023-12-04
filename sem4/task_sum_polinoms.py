# Задача 2 необязательная. Сумма многочленов как строк (Пользователь задает многочлены)
# Example: 3x^2 + 4x + 6 = 0, 4x^3 + 2x + 7 = 0

import re

def create_coeff_degree_dict(polinom):
    coeff_degree_dictionary = {}
    for index in range(len(polinom)):
        polinom[index].replace("=", "")
        polinom[index].replace("+", "")
        polinom[index].replace("-", "")
        polinom[index].replace("^", "")
        
        if index == len(polinom) - 1:
            exit()
        elif index % 2 == 0:
            coeff_degree_dictionary[polinom[index + 1]] = polinom[index]
        else:
            continue
        
    return coeff_degree_dictionary
        

first_polinom = input("Enter your first polinom: ")
second_polinom = input("Enter your second polinom: ")

regex = r'[+-^]?\d+(?:\.\d+)?'
first_symbols = re.findall(regex, first_polinom)
second_symbols = re.findall(regex, second_polinom)
print(first_symbols)
print(second_symbols)

print(create_coeff_degree_dict(first_symbols))
print(create_coeff_degree_dict(second_symbols))