from math import *

if __name__ == '__main__':
    a = [1, 2, 3, 4]
    b = [5, 6, 7, 8]
    c = list(map(lambda x, y: x+y, a, b))
    d = [(x+y) for x in a for y in b]
    print(c)
    print(d)
