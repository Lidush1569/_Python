import random


def generate_random_matrix(rows, cols):
    return [[random.randint(1, 100) for _ in range(cols)] for _ in range(rows)]


def get_column_sum(matrix, col_index):
    return sum(row[col_index] for row in matrix)


def get_row_average(matrix, row_index):
    row = matrix[row_index]
    return sum(row) / len(row) if row else 0


rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))
matrix = generate_random_matrix(rows, cols)

print("\nGenerated Matrix:")
for row in matrix:
    print(row)

row_index = int(input(f"\nEnter the row index (0 to {rows-1}): "))
col_index = int(input(f"Enter the column index (0 to {cols-1}): "))

row_avg = get_row_average(matrix, row_index)
col_sum = get_column_sum(matrix, col_index)

print(f"\nThe average of row {row_index} is: {row_avg}")
print(f"The sum of column {col_index} is: {col_sum}")
