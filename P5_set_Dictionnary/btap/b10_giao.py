from math import *

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = set(set(a).intersection(set(b)))
    for i in a:
        if i in c:
            print(i, end=' ')
            c.remove(i)
