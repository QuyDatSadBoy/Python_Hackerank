from math import *

if __name__ == '__main__':
    a, b = map(int, input().split())
    l = isqrt(a)
    if (l*l != a):
        l += 1
    r = isqrt(b)
    print(r-l+1)
