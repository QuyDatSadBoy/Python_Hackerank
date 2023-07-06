from math import *

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    t = int(input())
    while t:
        c, x = map(int, input().split())
        if c == 1:
            a.append(x)
        else:
            if c == 2:
                if x in a:
                    a.remove(x)
            else:
                if (x in a):
                    print("YES")
                else:
                    print("NO")
        t -= 1
