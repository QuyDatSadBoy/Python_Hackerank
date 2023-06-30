from math import *


def solve(n):
    if (n <= 9):
        return 1
    sum = 0
    return sum+1+solve(n//10)


if __name__ == '__main__':
    n = int(input())
    print(solve(n))
