from math import *

if __name__ == '__main__':
    a = list(range(1, 11, 1))
    print(a)
    b = a[0:4]
    c = a[-1:-11:-1]
    d = a[::-1]
    e = a[:]  # copy list
    f = a[-10:2]
    a[0:2] = []
    print("a sau khi xoa :")
    print(a)
    print("chen dau :")
    a[:0] = [13, 12, 2003]
    print(a)
    print("chen cuoi :")
    a[len(a):] = [20, 11, 2003]
    print(a)
    print("chen giua :")
    a[1:1] = ["okee"]
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print(f)
