from math import *

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    for i in a:
        sum = 0
        for j in i:
            sum += j
        print(sum, end=' ')
    print()
    for j in range(m):
        sum = 0
        for i in range(n):
            sum += a[i][j]
        print(sum, end=' ')
