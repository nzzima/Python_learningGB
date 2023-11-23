import random

length = int(input("Enter list length: "))

#numbers = [1, 21, 22, 2, 13, 5, 6, 15, 9, 10, 16, 18]
numbers = []
intermediate_seq = []
cont_increasing_seq = []

def create_random_list(len):
    for i in range (1, len + 1):
        numbers.append(random.randint(-5, 15))
        
def is_number_in_list(element, nums):
    if element in nums:
        return True
    return False
     
def find_increasing_sequence(nums):
    for temp in range(min(nums), max(nums) + 2):
        if is_number_in_list(temp, nums):
            intermediate_seq.append(temp)
        else:
            choose_increasing_sequence(intermediate_seq, cont_increasing_seq)
    
def choose_increasing_sequence(sequence, final_sequence):
    const_len = 0
    if len(sequence) == 0:
        exit
    elif len(sequence) == 1:
        sequence.clear()
    else:
        print(f"Found sequence --> {sequence}")
        if len(final_sequence) == 0:
            final_sequence.append(sequence[0])
            final_sequence.append(sequence[-1])
        elif sequence[-1] - sequence[0] > final_sequence[-1] - final_sequence[0]:
            final_sequence.clear()
            final_sequence.append(sequence[0])
            final_sequence.append(sequence[-1])
        elif sequence[-1] - sequence[0] < final_sequence[-1] - final_sequence[0] and len(final_sequence) < 4:
            exit
        else:
            final_sequence.append(sequence[0])
            final_sequence.append(sequence[-1])
        sequence.clear()

create_random_list(length)
print("Enter start list: ", numbers, "\n|==================================|")
find_increasing_sequence(numbers)
print("|==================================|", "\nFinal sequence = ", cont_increasing_seq)