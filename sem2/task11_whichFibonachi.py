# Which Fibonachi

A = int(input("Enter your number > 1: "))

fib1 = 1
fib2 = 1
print(f"{fib1} {fib2}", end=" ")

index = 3
check = False

for i in range(1, 2 * A):
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    print(fib_sum, end=" ")
    if A == fib_sum:
        check = True
        break
    elif fib_sum > 2 * A:
        break
    index += 1
    
    
if check == True:
    print(f"\nResult: {A} on place {index}")
else:
    print("\nResult: ",-1)