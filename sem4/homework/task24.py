import random

list_1 = list(random.randint(1, 5) for i in range(int(input("Введите количество кустов: "))))
print(list_1)

a = int(input("Введите номер куста: "))

result = 0
if a == 1:
    result = list_1[0] + list_1[1] + list_1[-1]
elif a == len(list_1):
    result = list_1[-2] + list_1[-1] + list_1[0]
else:
    result = list_1[a - 1] + list_1[a - 2] + list_1[a]
    
print(result)