import random


def generate_random_matrix(n, m):
    matrix = []
    for _ in range(n):
        n = [random.randint(1, 100) for _ in range(m)]
        matrix.append(n)
    return matrix


def get_column_sum(matrix, column_index):
    if not matrix:
        return 0
    if column_index < 0 or column_index >= len(matrix[0]):
        return 0
    return sum(n[column_index] for n in matrix)


def get_n_average(matrix, n_index):
    if not matrix:
        return 0
    if n_index < 0 or n_index >= len(matrix):
        return 0
    n = matrix[n_index]
    if not n:
        return 0
    return sum(n) / len(n)


matrix = generate_random_matrix(5, 6)
print("Random matrix:")
for n in matrix:
    print(n)

column_index = 3
column_sum = get_column_sum(matrix, column_index)
print(f"Sum of column {column_index}: {column_sum}")

n_index = 1
n_average = get_n_average(matrix, n_index)
print(f"Average of n {n_index}: {n_average}")
