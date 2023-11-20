import random

N = int(input("Enter count of numbers: "))

numbers = []

def create_random_list(len):
    for t in range (1, len):
        numbers.append(random.randint(1, 5))
        
def count_of_unic_num(number, data):
    count = 0
    for elem in data:
        if elem == number:
            count += 1
        else:
            continue
    return count

create_random_list(N)
print(numbers)
X = int(input("Enter unic number to count: "))
print(count_of_unic_num(X, numbers))