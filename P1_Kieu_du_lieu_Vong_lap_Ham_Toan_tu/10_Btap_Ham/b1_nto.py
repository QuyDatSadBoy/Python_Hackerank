from math import *


def nto(x):
    for i in range(2, isqrt(x)+1):
        if (x % i == 0):
            return False
    return x > 1


if __name__ == '__main__':
    n = int(input())
    if (nto(n)):
        print("YES")
    else:
        print("NO")
