from math import *


def sum(x):
    x = str(x)
    Sum = 0
    for i in x:
        Sum += ord(i)-48
    return Sum


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(key=lambda x: (sum(x), x))
    for i in a:
        print(i, end=' ')
