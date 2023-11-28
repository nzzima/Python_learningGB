import random

arr = [5, 8, 6, 4, 9, 2, 7, 3]

temp = 0
iteration = 0
result = []

while (temp < len(arr) - 1):
    if (temp == len(arr) - 1):
        iteration = arr[temp] + arr[temp - 1] + arr[0]
    else:
        iteration = arr[temp] + arr[temp - 1] + arr[temp + 1]
        result.append(iteration)
        result.sort()
    temp += 1

print(result[-1])