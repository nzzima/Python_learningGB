# Задача 8: Требуется определить, можно ли от шоколадки размером n × m
# отломить k
# долек, если разрешается сделать один разлом по
# прямой между дольками (то есть разломить шоколадку на два
# прямоугольника).

n = int(input("Enter n: "))
m = int(input("Enter m: "))
k = int(input("Enter k: "))

if k < n * m and ((k % n == 0) or (k % m == 0)):
    print('yes')
else:
    print('no')