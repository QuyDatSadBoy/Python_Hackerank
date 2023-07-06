from math import *

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a.sort(key=lambda x: abs(x))
    for i in a:
        print(i, end=' ')
