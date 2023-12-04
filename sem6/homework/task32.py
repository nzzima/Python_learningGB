import random

def min_to_max_inds(min_number, max_number, sp):
    result = []
    for index in range(len(sp)):
        if min_number <= sp[index] <= max_number:
            result.append(index)
        else:
            continue
    return result
            

N = int(input("Enter length for start_list: "))
min_number = int(input("Enter min_number: "))
max_number = int(input("Enter max_number: "))
start_list = [random.randint(-10, 10) for _ in range(N)]
print(start_list)
print(min_to_max_inds(min_number, max_number, start_list))

#or by generator
print([index for index in range(len(start_list)) if min_number <= start_list[index] <= max_number])