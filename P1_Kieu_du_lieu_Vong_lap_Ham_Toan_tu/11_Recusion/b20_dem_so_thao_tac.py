from math import *

ans = int(1e18+100)


def back_track(n, cnt):
    global ans
    if (cnt > ans):
        return
    if (n == 1):
        ans = min(ans, cnt)
        return
    if (n % 3 == 0):
        if (cnt+1 < ans):
            back_track(n//3, cnt+1)
    if (n % 2 == 0):
        if (cnt+1 < ans):
            back_track(n//2, cnt+1)
    if (n > 1):
        if (cnt+1 < ans):
            back_track(n-1, cnt+1)


if __name__ == '__main__':
    n = int(input())
    back_track(n, 0)
    print(ans)
