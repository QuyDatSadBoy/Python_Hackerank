from math import *


def solve():
    a, b = map(int, input().split())
    print(gcd(a, b), end=' ')
    print(lcm(a, b), end='')


if __name__ == '__main__':
    solve()
