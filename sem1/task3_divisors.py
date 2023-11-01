# Задача 3. Вывести все делители заданного числа

number = int(input("Enter yout number: "))

def all_divisors(number):
    for i in range(1, number + 1):
        if number % i == 0:
            print(f"{i} ")
        else: continue

all_divisors(number)