from math import *


def first_pos(a, i, x):
    res = -1
    l, r = i, len(a)-1
    while (l <= r):
        mid = (l+r)//2
        if (a[mid] > x):
            res = mid
            r = mid - 1
        else:
            l = mid+1
    return res


if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    res = 0
    for i in range(n-1):
        index = first_pos(a, i+1, k-a[i])
        if (index != -1):
            res += (n-index)
    print(res)
