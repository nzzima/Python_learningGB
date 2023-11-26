def get_count_all(sp):
    res = 0
    for item in sp:
        if isinstance(item, list):
            res += get_count_all(item)
        else:
            res += item
    return res

count_angola = 18
count_new_york = [20, [10, 7]]
count_chicago = 15
count_usa = [count_new_york,count_chicago ]
count_all = [count_angola, count_usa]
print(count_all)
print(get_count_all(count_all))