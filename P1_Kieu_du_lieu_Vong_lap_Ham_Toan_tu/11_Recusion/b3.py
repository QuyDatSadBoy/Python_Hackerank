from math import *


def sum(n):
    if (n == 1):
        return 1*(-1)**n
    return (-1)**n*n+sum(n-1)


if __name__ == '__main__':
    n = int(input())
    print(sum(n))
