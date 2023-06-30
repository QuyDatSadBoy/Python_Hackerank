from math import *


def solve(n):
    global ans
    if (n <= 9):
        ans = n
        return
    r = n % 10
    ans = r
    solve(n//10)


if __name__ == '__main__':
    ans = 0
    n = int(input())
    solve(n)
    print(ans)
