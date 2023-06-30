from math import *

if __name__ == '__main__':
    # ax + by = n
    a, b, n = map(int, input().split())
    # b: 0 -> n//a
    ok = False
    if (a == 0):
        if (b == 0):
            ok = True
        else:
            if n % b == 0 and (n/b >= 0):
                ok = True
    else:
        for i in range(0, n//a+1):
            tam = n-i*b
            x = tam/a
            if tam % a == 0 and x >= 0:
                ok = True
                break
    if (ok):
        print("YES")
    else:
        print("NO")
