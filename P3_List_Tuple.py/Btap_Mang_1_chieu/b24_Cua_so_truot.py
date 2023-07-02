from math import *

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    sum = 0
    for i in range(k):
        sum += a[i]
    print(sum, end=' ')
    for i in range(k, n):
        sum -= a[i-k]
        sum += a[i]
        print(sum, end=' ')
