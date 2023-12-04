def arih_progress(first, diff, count):
    for _ in range(count):
        print(first, end=" ")
        first += diff
    print()

first_element = int(input("Enter first element of arih_progression: "))
difference = int(input("Enter difference of arih_progression: "))
count_of_elements = int(input("Enter count of elements in arih_progression: "))

arih_progress(first_element, difference, count_of_elements)
#or
print(first_element, end=" ")
print(*[first_element := first_element + difference for _ in range(count_of_elements - 1)])