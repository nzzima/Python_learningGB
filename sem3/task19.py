# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.

# ---------------------СРЕЗЫ------------------------------------
# def move(input_list, pivot):
#     pivot = pivot % len(input_list)

#     left_list = input_list[:-pivot]
#     right_list = input_list[-pivot:]
#     moved_list = right_list + left_list 
#     return moved_list

# input_list = [1, 2, 3, 4, 5]
# k = 8

# print(move(input_list, k))
#----------------------------------------------------------

#--------------------------FOR-----------------------------
def move(input_list, pivot):
    pivot = pivot % len(input_list)
    
    for i in range(pivot):
        input_list.insert(0, input_list.pop())
    
    return input_list

input_list = [1, 2, 3, 4, 5]
k = 8
moved_list = move(input_list, k)
print(moved_list)
#------------------------------------------------------------