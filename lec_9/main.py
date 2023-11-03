class Matrix:
    def __init__(self, n, m):
        self.n = n
        self.m = m
        self.data = [[0 for _ in range(n)] for _ in range(m)]

    def __str__(self):
        matrix_str = ""
        for row in self.data:
            matrix_str += " ".join(map(str, row)) + "\n"
        return matrix_str

    def __add__(matrix1, matrix2):
        if matrix1.n == matrix2.n and matrix1.m == matrix2.m:
            result = Matrix(matrix1.n, matrix1.m)
            for i in range(matrix1.n):
                for j in range(matrix1.m):
                    result.data[i][j] = matrix1.data[i][j] + matrix2.data[i][j]
            return result
        else:
            raise ValueError("Matrix dimensions must match for addition")

    def __sub__(matrix1, matrix2):
        if matrix1.n == matrix2.n and matrix1.m == matrix2.m:
            result = Matrix(matrix1.n, matrix1.m)
            for i in range(matrix1.n):
                for j in range(matrix1.m):
                    result.data[i][j] = matrix1.data[i][j] - matrix2.data[i][j]
            return result
        else:
            raise ValueError("Matrix dimensions must match for subtraction")

    def __mul__(matrix1, matrix2):
        if matrix1.n == matrix2.m:
            result = Matrix(matrix1.n, matrix2.m)
            for i in range(matrix1.n):
                for j in range(matrix2.m):
                    total = 0
                    for k in range(matrix1.m):
                        total += matrix1.data[i][k] * matrix2.data[k][j]
                    result.data[i][j] = total
            return result
        else:
            raise ValueError("Number of columns in the first matrix must match the number of rows in the second matrix for multiplication")


# Example usage:
matrix1 = Matrix(2, 2)
matrix1.data = [[2, 3], [5, 6]]

matrix2 = Matrix(2, 2)
matrix2.data = [[8, 9], [11, 12]]

# Addition
result_add = matrix1 + matrix2
print("Addition:")
print(result_add)

matrix3 = Matrix(2, 2)
matrix3.data = [[1, 2], [3, 4]]

matrix4 = Matrix(2, 2)
matrix4.data = [[5, 6], [7, 8]]

# Subtraction
result_sub = matrix3 - matrix4
print("Subtraction:")
print(result_sub)

matrix5 = Matrix(2, 2)
matrix5.data = [[3, 4], [5, 6]]

matrix6 = Matrix(2, 2)
matrix6.data = [[9, 10], [13, 14]]

# Multiplication
result_mul = matrix5 * matrix6
print("Multiplication:")
print(result_mul)
