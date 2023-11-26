# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

def replace_max_to_min(sp, index, maximum):
    if index == len(sp):
        return
    if sp[index] == maximum:
        sp[index] = min(sp)
    return replace_max_to_min(sp, index + 1, maximum)


sp = [1, 4, 4, 3, 3]
max_num = max(sp)
print(sp)
# for i in range(len(sp)):
#     if sp[i] == max(sp):
#         sp[i] = min(sp)    

replace_max_to_min(sp, 0, max_num)
print(sp)