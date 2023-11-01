# Задача 2. Посчитать количество цифр любого целого или вещественного числа.
# Число вводит пользователь. Через строку решать нельзя.

number = float(input("Enter your number: "))
start_num = number

count = 1
while number != int(number):
    number *= 10
    count += 1
    
print(number)

if start_num < 1:
    print(count)
elif number > 1:
    sum = 0
    while number > 0:
        sum += 1
        number //= 10
    print(sum)