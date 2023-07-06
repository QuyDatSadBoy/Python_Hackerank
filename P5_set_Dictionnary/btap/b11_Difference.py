from math import *

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = map(int, input().split())
    b = map(int, input().split())
    a = list(set(a).difference(set(b)))
    a.sort()
    for i in a:
        print(i, end=' ')
