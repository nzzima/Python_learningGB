def in_degree(num1, num2):
    if num2 == 0:
        return 1
    else:
        return num1 * in_degree(num1, num2 - 1)

A = int(input("Task A^B:\nEnter number: "))
B = int(input("Enter degree: "))

print(in_degree(A, B))