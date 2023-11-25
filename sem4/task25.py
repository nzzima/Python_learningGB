# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.

# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2

# Для решения данной задачи используйте функцию
# .split()

start_ = 'a a a b c a a d c d d'
intermediate_array = ''
start_ = start_.split(' ')

for i in start_:
    count_elem = intermediate_array.count(i)
    #print(count_elem)
    if count_elem == 0:
        intermediate_array += i + ' '
    else:
        intermediate_array += i + '_' + str(count_elem) + ' '
        
print(intermediate_array.strip())