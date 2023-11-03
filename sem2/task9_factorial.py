# Factorial by while

n = int(input("Enter your number to calculate factorial: "))

temp = 1
fact = 1
while temp <= n:
    fact *= temp
    temp += 1
print(f"Factorial of {n} is {fact}")