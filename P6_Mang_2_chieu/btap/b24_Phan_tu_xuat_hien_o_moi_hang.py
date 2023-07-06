from math import *

if __name__ == '__main__':
    n = int(input())
    a = []
    mp = dict({})
    mp = {x: 0 for x in range(0, 101)}
    for i in range(n):
        a.append(list(map(int, input().split())))
    for i in range(n):
        for j in range(n):
            if (i == 0):
                mp[a[i][j]] = i+1
            else:
                if mp[a[i][j]] == i:
                    mp[a[i][j]] = i+1
    ok = False
    a[n-1].sort()
    for i in range(n):
        if mp[a[n-1][i]] == n:
            print(a[n-1][i], end=' ')
            mp[a[n-1][i]] = 0
            ok = True
    if (not ok):
        print("NOT FOUND")
