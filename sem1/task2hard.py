# Задача 2. Посчитать количество цифр любого целого или вещественного числа.
# Число вводит пользователь. Через строку решать нельзя.

number = float(input("Enter your number: "))

while number != int(number):
    number *= 10
    
print(number)
    
sum = 0
while number > 0:
    sum += 1
    number //= 10
    
print(int(sum))