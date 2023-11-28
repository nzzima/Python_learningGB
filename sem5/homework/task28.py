def sum(a, b):
    if a == 0:
        return b
    else:
        return sum(a - 1, b + 1)
    

A = int(input("Task A + B:\nEnter number1: "))
B = int(input("Enter number2: "))

print(sum(A, B))