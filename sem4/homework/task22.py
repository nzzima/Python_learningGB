def enter_sequence(array, length):
    for index in range(length):
        array.append(input(f"Enter {index+1} element: "))

def append_unique_nums(first_seq, second_seq):
    final_seq = []
    if len(first_seq) >= len(second_seq):
        for index in range(len(first_seq)):
            if first_seq[index] in second_seq and first_seq[index] not in final_seq:
                final_seq.append(first_seq[index])
                #print(first_seq[index])
            else:
                continue
    elif len(first_seq) < len(second_seq):
        for index in range(len(second_seq)):
            if second_seq[index] in first_seq and second_seq[index] not in final_seq:
                final_seq.append(second_seq[index])
                #print(second_seq[index])
    return final_seq

first_sequence = []
second_sequence = []

n = int(input("Enter first length: "))      
enter_sequence(first_sequence, n)
m = int(input("Enter second length: "))
enter_sequence(second_sequence, m)

#print(first_sequence)
#print(second_sequence)
final_sequence = append_unique_nums(first_sequence, second_sequence)
final_sequence.sort()
print(final_sequence)