# Задача 1. Посчитать сумму цифр любого целого или вещественоего числа. 
# Число вводит пользователь (Через строку решать нельзя)

number = float(input("Enter your number: "))

while number != int(number):
    number *= 10
    
print(number)
    
sum = 0
while number > 0:
    sum += number % 10
    number //= 10
    
print(int(sum))