from math import *


def solve(n):
    if (n == 0):
        return
    r = n % 16
    solve(n//16)
    if (r < 10):
        print(r, end='')
    else:
        print(chr(ord('A')+r-10), end='')


if __name__ == '__main__':
    n = int(input())
    if (n == 0):
        print(0)
    else:
        solve(n)
