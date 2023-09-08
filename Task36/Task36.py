def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        row = []
        for j in range(1, num_columns + 1):
            element = operation(i, j)
            row.append(str(element))
        print(' '.join(row))

# Пример использования
print_operation_table(lambda x, y: x * y)