from math import *

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    i, j = 0, 0
    while i < n and j < m:
        if (a[i] <= b[j]):
            print("b%d" % (i+1), end=' ')
            i += 1
        else:
            print("c%d" % (j+1), end=' ')
            j += 1
    while i < n:
        print("b%d" % (i+1), end=' ')
        i += 1
    while j < m:
        print("c%d" % (j+1), end=' ')
        j += 1
