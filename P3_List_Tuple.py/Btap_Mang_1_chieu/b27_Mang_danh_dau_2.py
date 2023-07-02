from math import *

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    f = [0]*(10**6+1)
    for i in a:
        f[i] += 1
    for i in range(0, 10**6+1):
        if (f[i] != 0):
            print(i, f[i])
