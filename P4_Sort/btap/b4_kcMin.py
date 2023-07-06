from math import *

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    res = 10**18+1
    a.sort()
    for i in range(1, n):
        res = min(res, a[i]-a[i-1])
    print(res)
