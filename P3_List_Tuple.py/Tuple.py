from math import *

if __name__ == '__main__':
    a = (1, 2)
    b = ("tran", "quy", "dat")
    c = (13,)
    print(type(a), type(b), type(c))
    d = tuple(range(1, 5))
    e, *f = d
    print(e, f)
    print(type(e))
    print(type(f))
