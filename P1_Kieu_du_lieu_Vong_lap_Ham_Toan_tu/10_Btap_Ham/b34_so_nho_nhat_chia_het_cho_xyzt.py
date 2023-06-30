from math import *

if __name__ == '__main__':
    a, b, c, n = map(int, input().split())
    l = 10**(n-1)
    tam = lcm(a, b, c)
    ans = (l+tam-1)//tam*tam
    if (ans < 10**(n)):
        print(ans)
    else:
        print(-1)
