from math import *

if __name__ == '__main__':
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ok = False
    for i in range(n-1):
        b = a[i+1:]
        if (a[i]+x) in b:
            print(1)
            ok = True
            break
    if (not ok):
        print(-1)
