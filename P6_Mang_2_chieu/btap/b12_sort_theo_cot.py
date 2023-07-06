from math import *

if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    b = []
    for j in range(n):
        c = []
        for i in range(n):
            c.append(a[i][j])
        c.sort()
        b.append(c)
    for i in range(n):
        for j in range(n):
            print(b[j][i], end=' ')
        print()
