from math import *

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a = set(a)
    t = int(input())
    while t:
        x = int(input())
        if x in a:
            print("YES")
        else:
            print("NO")
        t -= 1
