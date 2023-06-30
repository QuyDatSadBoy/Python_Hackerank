from math import *


def solve(n):
    if (n <= 9):
        return n
    sum = 0
    r = n % 10
    return sum+r+solve(n//10)


if __name__ == '__main__':
    n = int(input())
    print(solve(n))
