from math import *


def nto(n):
    for i in range(2, isqrt(n)+1):
        if (n % i == 0):
            return False
    return n > 1


def check(n):
    for i in range(2, 33):
        if (nto(i)):
            tam = 2**i-1
            if (nto(tam)):
                hh = tam*(2**(i-1))
                if (hh == n):
                    return True
    return False


if __name__ == '__main__':
    n = int(input())
    if (check(n)):
        print("YES")
    else:
        print("NO")
