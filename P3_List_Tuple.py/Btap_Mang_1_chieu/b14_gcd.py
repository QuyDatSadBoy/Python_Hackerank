from math import *

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    res = 0
    for i in a:
        res = gcd(res, i)
    print(res)
