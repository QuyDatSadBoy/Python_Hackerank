from math import *

if __name__ == '__main__':
    n, m = map(int, input().split())
    a = [[0 for _ in range(m)] for _ in range(n)]
    print(a)

    c = []
    T = int(input())
    for i in range(T):
        d = list(map(int, input().split()))
        c.append(d)
    print(c)
