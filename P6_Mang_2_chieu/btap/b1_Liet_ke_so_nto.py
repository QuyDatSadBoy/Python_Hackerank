from math import *


def nto(n):
    for i in range(2, isqrt(n)+1):
        if (n % i == 0):
            return False
    return n > 1


if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    for i in a:
        for j in i:
            if (nto(j)):
                print(j, end=' ')
        print()
