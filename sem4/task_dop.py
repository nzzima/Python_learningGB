# Задача 1 необязательная.
# Пользователь вводит натуральное k. Надо сформировать многочлен такой степени, где все коэффициенты 
# случайные от -10 до 10.
# ​
# например, k=2 -> -x^2 + 3*x - 8 = 0
# тут коэффициенты -1,3,-8
# например, k=3 -> 3*x^3 - 2*x = 0
# тут коэффициенты 3,0,-2,0
import random

k = int(input("Enter degree: "))

def create_polinom(degree):
    temp = degree
    polinom = ""
    coefficients = [random.randint(-10, 10) for _ in range(degree + 1)]
    print(coefficients)
    for coeff in coefficients:
        if coeff != 0:
            if coeff > 0 and temp == degree:
                polinom += f"{coeff}*x^{degree} "
            elif coeff > 0 and temp != degree:
                polinom += f"+ {coeff}*x^{degree} "
            else:
                polinom += f"{coeff}*x^{degree} "
            degree -= 1
        elif coeff == 0:
            degree -= 1
            continue
    polinom = polinom.replace('x^1', 'x')
    polinom = polinom.replace('*x^0', '')
    polinom += "= 0"
    return polinom
        
print(create_polinom(k))
    
    