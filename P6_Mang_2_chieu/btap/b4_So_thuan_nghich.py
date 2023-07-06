from math import *


def check(n):
    n = str(n)
    if (n == n[::-1]):
        return True
    return False


if __name__ == '__main__':
    n = int(input())
    a = []
    for i in range(n):
        a.append(list(map(int, input().split())))
    cnt = 0
    for i in range(n):
        for j in range(i+1):
            if (check(a[i][j])):
                cnt += 1
    print(cnt)
