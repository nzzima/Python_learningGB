# Задача: Даны два массива чисел. Требуется вывести те элементы
# первого массива (в том порядке, в каком они идут в первом
# массиве), которых нет во втором массиве. 

import random

N = int(input("Enter length: "))

list1 = [random.randint(0, 11) for i in range(N)]
list2 = [random.randint(0, 11) for i in range(N)]

print(list1)
print(list2)
print(*[i for i in list1 if i not in set(list2)])

# from random import randint


# print( randMassive1:= [randint(-5,10) for _ in range(5)] )
# print( randMassive2:= [randint(-5,10) for _ in range(5)] )

# print([i for i in randMassive1 if i not in randMassive2])