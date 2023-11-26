# Посчитать сумму всех натуральных чисел от 1 до n.

def summa_cycle(n):
    res = 0
    while True:
        if n == 0:
            break
        res += n
        n -= 1
    return res

def summa_rec(n):
    if n == 0:
        return 0
    return n + summa_rec(n - 1)

# Погружение:
# summa_rec(4) = (4 + (3 + (2 + (1 + 0))))
# Всплытие:
# (4 + (3 + (2 + (1 + 0)))) = 4 + (3 + 3) = 10

n = int(input("Enter your number: "))
print(summa_cycle(n))
print(summa_rec(n))