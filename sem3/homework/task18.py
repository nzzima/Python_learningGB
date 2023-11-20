import random

N = int(input("Enter count of numbers: "))

numbers = []
data = []

def create_random_list(len):
    for t in range (1, len):
        numbers.append(random.randint(1, 5))
        
def the_closest_num(num, numbers): # 1 var
    min_diff = float('inf')
    closest = None
    for elem in numbers:
        diff = abs(elem - num)
        if diff < min_diff:
            min_diff = diff
            closest = elem
    return closest
        
        
create_random_list(N)
print(numbers)
X = int(input("Enter your number: "))
the_closest_num(X, numbers)
print(the_closest_num(X, numbers))

print(min(numbers, key=lambda a:abs(a - X))) # 2 var


    