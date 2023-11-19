# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.

def get_set(list):
    # print(set(list))
    return len(set(list))

input_list = [1, 1, 2, 0, -1, 3, 4, 4]
print(get_set(input_list))