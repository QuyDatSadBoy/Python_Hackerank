import pandas as pd
import numpy as np
from IPython.display import display

if __name__ == '__main__':
    data = pd.read_csv("P4AI_BT1.csv")
    print("Danh sách các bản ghi có speal.length > 5:")
    print(data.query("`sepal.length` > 5"))
    print("Danh sách các bản ghi có speal.width > 3:")
    print(data.query('`sepal.width` > 3'))

    # Cách 2
    # print("Danh sách các bản ghi có speal.length > 5:")
    # print(data[data["sepal.length"] > 5])
    # print("Danh sách các bản ghi có speal.width > 3:")
    # print(data[data["sepal.width"] > 3])

    # Giải thích cách 2
    # Đây là cách sử dụng indexing (cắt lát) của DataFrame để truy vấn và in ra
    #  các hàng trong data mà giá trị của cột "sepal.length" lớn hơn 5.
    # Kết quả trả về là một DataFrame mới chỉ chứa các hàng thỏa mãn điều kiện.
