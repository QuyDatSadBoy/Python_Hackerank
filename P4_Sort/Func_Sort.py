from math import *
from operator import itemgetter
from functools import cmp_to_key
from bisect import *


def cmp(a, b):
    return b-a


if __name__ == '__main__':
    a = [["Dat", 1000], ["An", 100], ["Khanh", 5000]]
    # a.sort(key=lambda x: x[1])
    a.sort(key=itemgetter(1, 0))
    print(a)
    b = list(range(1, 6))
    b.sort(key=cmp_to_key(cmp))
    print(b)

    my_list = [1, 3, 5, 5, 7, 9]

    # Tìm vị trí chèn (lower bound) của số 5 trong danh sách
    print(bisect(my_list, 5))
    lower_bound = bisect_left(my_list, 5)
    print(lower_bound)  # Output: 2

    # Tìm vị trí chèn (upper bound) của số 5 trong danh sách
    upper_bound = bisect_right(my_list, 5)
    print(upper_bound)  # Output: 4

    print(bisect(my_list, 2))
    lower_bound = bisect_left(my_list, 2)
    print(lower_bound)  # Output: 2

    # Tìm vị trí chèn (upper bound) của số 5 trong danh sách
    upper_bound = bisect_right(my_list, 2)
    print(upper_bound)  # Output: 4
