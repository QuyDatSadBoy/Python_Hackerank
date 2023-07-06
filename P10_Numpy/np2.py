import numpy as np

if __name__ == "__main__":
    a = np.array([1, 2, 3, 4, 5, 6])
    # gan lai thanh 3 hang 4 cot
    # a = a.reshape(2, 3)
    # print(a)
    a2 = np.array([[1, 2, 3], [4, 5, 6]])
    a2 = a2.reshape(-1)
    # hoac a2 = a2.flatten()
    a2 = np.append(a2, 7)
    print(a2)
    arr = np.concatenate((a, a2))
    print(arr)
    # search
    arr1 = np.array([1, 2, 3, 4, 5, 6])
    res = np.where(arr1 % 2 == 0)
    print(arr1[res])
    print(res)
