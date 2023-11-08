import random
import math

S = int(input("Enter summ of numbers X and Y: ")) # S = X + Y => X = S - Y
P = int(input("Enter multiplication of numbers X and Y: ")) # P = X * Y => P = (S - Y) * Y => P = S*Y - Y*Y
                                                            # => Y*Y - S*Y + P = 0 like ax2 + bx + c = 0
                                                            # b2 - 4ac = D => S*S - 4*1*P = D
                                                            # Y = (S +- sqrt(D))/2

X = 0
Y = 0

def check(num1, num2):
    if num1 > 1000 and num2 > 1000:
        print("Incorrect numbers. Try again.")
        return
    
def isint(num):
    try:
        int(num)
        return True
    except ValueError:
        return False
    
def get_numbers(sum, multiplic):
    y = 0
    discrem = sum * sum - 4 * multiplic
    if discrem == 0:
        y = sum / 2
    elif discrem > 0:
        y1 = (sum + math.sqrt(discrem))/2
        y2 = (sum - math.sqrt(discrem))/2
        if isint(y1):
            y = y1
        elif isint(y2):
            y = y2
        else:
            print("Incorrect sum and multiplication. Try again")
            exit()
    elif discrem < 0:
        print("Incorrect sum and multiplication. Try again")
        exit()
    return y

Y = get_numbers(S, P)
X = S - Y

print(f"Numbers: X = {int(X)}, Y = {int(Y)}")