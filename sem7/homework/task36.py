def print_operation_table(operation, num_rows, num_columns):
    if num_rows < 2 or num_columns < 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        header = ' '.join([str(i) for i in range(1, num_columns + 1)])
        print(header)
        for i in range(2, num_rows + 1):
            row = [str(i)] + [str(operation(i, j)) for j in range(2, num_columns + 1)]
            print(' '.join(row))

        
print_operation_table(lambda x, y: x * y, 3, 3)
print()
print_operation_table(lambda x, y: x + y, 4, 4)
print()
print_operation_table(lambda x, y: x - y, 4, 4)

