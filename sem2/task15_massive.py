import random

N = int(input("Enter number of watermelons: "))
watermelons = []

def rnd_mass_of_watermelons(N):
    for i in range(N):
        watermelons.append(random.randint(1, 10))

def find_max(data):
    max = 0
    for item in data:
        if item > max:
            max = item
    return max

def find_min(data):
    min = 10
    for item in data:
        if item < min:
            min = item
    return min

rnd_mass_of_watermelons(N)
print(watermelons)
print(f"Watermelon for me: {find_max(watermelons)} kg, for she {find_min(watermelons)} kg")