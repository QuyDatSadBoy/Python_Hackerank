from math import *

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    f = [0]*n
    for i in (range(0, n)):
        if (i == 0):
            f[i] = a[i]
        else:
            f[i] = f[i-1]+a[i]
    for i in f:
        print(i, end=' ')
