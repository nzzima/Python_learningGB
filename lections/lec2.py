"""Lection 2
:list
:tuple
:dictionary
"""

# Списки
list1 = []
print(list1)
list1 = list()
print(list1)
list1 = [1, 2, 3, 4]
print(list1)

# Срезы
list2 = [1,2,3,4,5,6,7,8,9,10]
print(list2[:])
print(list2[:2])    # [1, 2]
print(list2[2:])    # [3,4,5,6,7,8,9,10]
print(list2[2:9])   # [3,4,5,6,7,8,9]
print(list2[6:-1])  # [7,8,9]
print(list2[2::9])  # [3]

# Кортежи
t = ()
print(type(t))

t = (1, 5, 3, )
print(type(t))

v = [1, 8, 9]
print(v)
print(type(v))

v = tuple(v)
print(type(v))

a, b, c = v
print(a, b, c)

tup = (1, 2, 3, 4)
for i in range(len(tup)):
    print(tup[i])
    
# Словари
dictionary = {}
dictionary = {'q':'qwerty', 'w':'werty', 'e':'erty'}
print(dictionary)
dictionary[890] = 32778
print(dictionary)

print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
for item in dictionary:
    print('{}: {}'.format(item, dictionary[item]))
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
for item in dictionary:
    print(item)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
for (k,v) in dictionary.items():
    print(k, v)
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print(dictionary.items())
print("++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")