from math import *
from collections import Counter

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    res, cnt = -1, 0
    a = list(Counter(a).items())
    for x, y in a:
        if (y > cnt):
            cnt = y
            res = x
        else:
            if y == cnt:
                if (x < res):
                    res = x
    print(res, cnt)
