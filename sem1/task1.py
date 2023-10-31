# Задача 2: Найдите сумму цифр трехзначного числа.

number = int(input("Enter your number: "))

a = number % 10
b = (number // 10) % 10
c = number // 10

print(f"Result = {a + b + c}")