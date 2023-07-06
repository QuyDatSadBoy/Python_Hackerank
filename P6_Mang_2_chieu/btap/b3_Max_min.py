from math import *

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    Min = 10**18+9
    Max = -(10**18+9)
    for i in a:
        Min = min(Min, min(i))
        Max = max(Max, max(i))
    print(Min)
    for i in range(n):
        for j in range(m):
            if (a[i][j] == Min):
                print(i+1, j+1)
    print(Max)
    for i in range(n):
        for j in range(m):
            if (a[i][j] == Max):
                print(i+1, j+1)
