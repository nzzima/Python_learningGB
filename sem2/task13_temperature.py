import random

N = int(input("Enter number of days: "))

days = []
checkpoint_list = []

def rnd_day_list(n):
    for i in range(1, n):
        days.append(random.randint(-50, 50))
    
def create_check_list(days, n):
    checking_point = 0
    for day in days:
        if day > 0:
            checking_point += 1     
        elif day <= 0:
            if checking_point > 0:
                checkpoint_list.append(checking_point)
            checking_point = 0
    if checking_point > 0:
        checkpoint_list.append(checking_point)

def find_max(data):
    max = 0
    for item in data:
        if item > max:
            max = item
    return max

rnd_day_list(N)
create_check_list(days, N)
print(days)
print(checkpoint_list)
max_elem = find_max(checkpoint_list)
print(f"Max days with positive temperature: {max_elem}")