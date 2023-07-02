from math import *

if __name__ == '__main__':
    a = set([1, 2, 3, 4, 5])
    b = set([6, 7, 8, 9, 10])
    c = a | b
    print(c)
    a.update(b)
    d = a
    print(d)
