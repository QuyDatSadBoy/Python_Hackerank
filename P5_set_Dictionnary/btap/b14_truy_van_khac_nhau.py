from math import *

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    se = set({})
    se.add(a[n-1])
    f = [1]*n
    for i in range(n-2, -1, -1):
        if not (a[i] in se):
            f[i] = f[i+1]+1
            se.add(a[i])
        else:
            f[i] = f[i+1]
    T = int(input())
    while T:
        x = int(input())
        print(f[x])
        T -= 1
