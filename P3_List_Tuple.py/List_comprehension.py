from math import *

if __name__ == '__main__':
    def change(l): return [x for x in l if x >= 0]
    a = [1, 2, -3, -4, 5, -10, 12]
    print(change(a))
    print(a)

    def flatten(big_list): return [
        item for small_list in big_list for item in small_list]
    a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(flatten(a))

    b = list(range(1, 6))
    c = [x**2 for x in b if x % 2 == 0]
    print("c=")
    print(c)
    def func(d): return [x**3 for x in d if x % 2 == 0]
    print(func(b))
