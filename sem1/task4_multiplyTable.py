# Задача 4. Вывести таблицу умножения как в школьной тетради

for j in range(2, 11):
    for i in range (2, 6):
        print(i, "*", j, "=", i * j, end="\t")
    print()
    
print()
    
for j in range(2, 11):
    for i in range (6, 10):
        print(i, "*", j, "=", i * j, end="\t")
    print()