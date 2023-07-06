from math import *

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a.extend(b)
    a = list(set(a))
    a.sort(reverse=True)
    for i in a:
        print(i, end=' ')
