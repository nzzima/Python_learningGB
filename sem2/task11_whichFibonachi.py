# Which Fibonachi

A = int(input("Enter your number > 1: "))

fib1 = 1
fib2 = 1
print(f"{fib1} {fib2}", end=" ")

index = 0
check = False

for i in range(1, 2 * A):
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    index = i + 1
    print(fib_sum, end=" ")
    if A == fib_sum:
        check = True
        break
    elif fib_sum > 2 * A:
        break
    
if check == True:
    print(f"\nResult: {A} on the place {index}")
else:
    print("\nResult: ",-1)