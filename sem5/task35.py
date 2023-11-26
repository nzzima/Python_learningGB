# Напишите функцию, которая принимает одно число и 
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое 
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes 

number = int(input("Enter number: "))

def is_simple_num(num, div = None):
    if div is None:
        div = num - 1
    while div >= 2:
        if num % div == 0:
            return False
        else:
            return is_simple_num(num, div - 1)
    else:
        return True
    
if is_simple_num(number):
    print("Simple")
else:
    print("Not simple")       

# count = 0 
# for i in range(num):
#     if num % i == 0:
#         count += 1
# if count == 2:
#     return num