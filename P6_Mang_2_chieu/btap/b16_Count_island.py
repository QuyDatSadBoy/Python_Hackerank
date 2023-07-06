from math import *

a = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def back_track(i, j):
    global a, dx, dy, n, m
    a[i][j] = 0
    for k in range(4):
        imoi = i + dx[k]
        jmoi = j + dy[k]
        if (imoi >= 0 and imoi < n and jmoi >= 0 and jmoi < m and a[imoi][jmoi] == 1):
            back_track(imoi, jmoi)


if __name__ == '__main__':
    n, m = map(int, input().split())
    for i in range(n):
        a.append(list(map(int, input().split())))
    cnt = 0
    for i in range(n):
        for j in range(m):
            if (a[i][j] == 1):
                cnt += 1
                back_track(i, j)
    print(cnt)
