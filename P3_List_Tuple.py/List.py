from math import *

if __name__ == '__main__':
    a = [13, 12, 2003]
    b = list(a)
    b.reverse()
    print(a)
    print(b)
    print(b is a)
    print("a[0]=", a[0])
    print("a[-1]=", a[-1])
    a += b
    a.append(20)
    a.insert(0, 1000)  # them duoc 1 phan tu
    a.pop()
    del (a[1])
    a.remove(1000)
    print("idex 12 = ", a.index(12))
    print("Duyet list:")
    c = [0]*10
    print("len c =", len(c))
    for i in a:
        print("%d" % i, end=' ')
    print()
    d = [1, 2, 3, 4]
    print("Duyet list nguoc: ")
    for i in range(len(d)-1, -1, -1):
        print(d[i])
