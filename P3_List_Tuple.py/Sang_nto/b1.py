from math import *

mod = 10**9+7
f = [1]*(10**6+1)
for i in range(2, 10**6+1):
    f[i] = f[i-1]*i
    f[i] %= mod
if __name__ == '__main__':
    t = int(input())
    while t:
        n = int(input())
        print(f[n])
        t -= 1
