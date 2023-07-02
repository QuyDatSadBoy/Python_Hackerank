# Định nghĩa hai ma trận
matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[10, 11, 12],
           [13, 14, 15],
           [16, 17, 18]]


def add_matrices(matrix1, matrix2):
    result = list(map(lambda row1, row2: list(
        map(lambda x, y: x + y, row1, row2)), matrix1, matrix2))
    return result


result_matrix = add_matrices(matrix1, matrix2)
for row in result_matrix:
    print(row)
