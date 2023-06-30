from math import *


def solve(n):
    if (n == 0):
        return
    r = n % 2
    solve(n//2)
    print(r, end='')


if __name__ == '__main__':
    n = int(input())
    if (n == 0):
        print(0)
    else:
        solve(n)
