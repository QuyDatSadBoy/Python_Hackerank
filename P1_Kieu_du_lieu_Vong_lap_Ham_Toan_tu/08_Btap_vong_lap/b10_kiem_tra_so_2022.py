from math import *
if __name__ == '__main__':
    n = int(input())
    ok = False
    list = list(map(int, input().split()))
    for i in list:
        if (i == 2022):
            ok = True
            break
    if (ok):
        print("YES")
    else:
        print("NO")
