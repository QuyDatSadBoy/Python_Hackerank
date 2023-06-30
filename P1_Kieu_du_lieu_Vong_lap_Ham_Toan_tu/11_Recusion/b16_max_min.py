from math import *

Min = 11
Max = -1


def solve(n):
    global Min, Max
    if (n <= 9):
        Min = min(Min, n)
        Max = max(Max, n)
        return
    r = n % 10
    Min = min(Min, r)
    Max = max(Max, r)
    solve(n//10)


if __name__ == '__main__':
    n = int(input())
    solve(n)
    print(Max, Min)
