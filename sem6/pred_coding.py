import random

def create_list(lower, upper, count):
    res = []
    for _ in range(count):
        res.append(random.randint(lower, upper))
    return res

sp = [i for i in range(10)]
print(sp)

print([i**2 for i in sp])
print([i**2 for i in sp if i%2])
print([i**2 if i%2 else 0 for i in sp])
print(sum([i**2 if i%2 else 0 for i in sp]))

print({i: chr(i) for i in range(5)})