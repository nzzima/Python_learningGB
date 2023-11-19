# Задача НЕГАФИБОНАЧЧИ по желанию
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

def fibs(num):
    nums_pos = [0, 1]
    nums_neg = [0, 1]
    for i in range(num - 1):
        nums_pos.append(nums_pos[i] + nums_pos[i + 1])
        nums_neg.append(nums_neg[i] - nums_neg[i + 1])
    return (nums_neg[:0:-1] + nums_pos)

print(fibs(8))