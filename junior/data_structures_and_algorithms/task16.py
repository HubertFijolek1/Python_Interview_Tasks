### 16. **Function that rotates a matrix (2D list) by 90 degrees**

def rotate_matrix(matrix):
    return [list(reversed(col)) for col in zip(*matrix)]

def rotate_matrix_inplace(matrix):
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            temp = matrix[i][j]
            matrix[i][j] = matrix[n - 1 - j][i]
            matrix[n - 1 - j][i] = matrix[n - 1 - i][n - 1 - j]
            matrix[n - 1 - i][n - 1 - j] = matrix[j][n - 1 - i]
            matrix[j][n - 1 - i] = temp
    return matrix

def rotate_matrix_transpose_reverse(matrix):
    matrix[:] = [list(row) for row in zip(*matrix)]
    for row in matrix:
        row.reverse()
    return matrix
