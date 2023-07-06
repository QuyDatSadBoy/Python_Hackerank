from math import *

if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    cnt = 0
    for i in range(n):
        a[i][i], a[i][n-i-1] = a[i][n-i-1], a[i][i]
    for i in range(n):
        for j in range(n):
            print(a[i][j], end=' ')
        print()
