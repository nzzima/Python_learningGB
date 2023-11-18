# Which Fibonachi

m = int(input("Введите число больше 1: "))

f_0 = 0
f_1 = 1
f_2 = 1
n = 3
while f_2 < m:
    f_0 = f_1
    f_1 = f_2
    f_2 = f_0 + f_1
    n += 1
    if m == f_2:
        print(f"Fibonachi! Index = {n}")
    elif f_2 > m:
        if abs(m - f_2) > abs(m - f_1):
            print(f"Not Fibonachi, but closer to is {f_1}")
        else:
            print(f"Not Fibonachi, but closer to is {f_2}")