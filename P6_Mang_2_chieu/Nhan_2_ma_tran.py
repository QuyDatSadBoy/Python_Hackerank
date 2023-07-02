matrix1 = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

matrix2 = [[10, 11],
           [12, 13],
           [14, 15]]

# Hàm nhân hai ma trận


def multiply_matrices(matrix1, matrix2):
    # Xác định số hàng và số cột của hai ma trận
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    # Kiểm tra tính hợp lệ của phép nhân ma trận
    if cols1 != rows2:
        print("Không thể nhân hai ma trận. Số cột của ma trận thứ nhất phải bằng số hàng của ma trận thứ hai.")
        return None

    # Tạo ma trận kết quả với các phần tử ban đầu là 0
    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    # Tính tích của từng phần tử trong ma trận
    for i in range(rows1):
        for j in range(cols2):
            result[i][j] = sum(
                map(lambda x, y: x * y, matrix1[i], [cols2[j] for row in matrix2]))

    return result


# Gọi hàm nhân hai ma trận và in kết quả
result_matrix = multiply_matrices(matrix1, matrix2)
if result_matrix is not None:
    for row in result_matrix:
        print(row)
