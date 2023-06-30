from math import *


def nto(n):
    for i in range(2, isqrt(n)+1):
        if (n % i == 0):
            return False
    return n > 2


if __name__ == '__main__':
    l, r = map(int, input().split())
    l1 = isqrt(l)
    if (l1**2 != l):
        l1 += 1
    r1 = isqrt(r)
    for i in range(l1, r1+1, 1):
        if (nto(i)):
            print(i*i, sep=' ')
