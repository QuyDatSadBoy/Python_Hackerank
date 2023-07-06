from math import *

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a = set(a)
    T = int(input())
    while T > 0:
        x = int(input())
        if x in a:
            print('YES')
        else:
            print('NO')
        T -= 1
