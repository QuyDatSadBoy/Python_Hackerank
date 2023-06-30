from math import *
if __name__ == '__main__':
    a = int(input())
    cnt = a//28
    a = a//28
    while a > 2:
        cnt += a//3
        r = a % 3
        a = a//3+r
    print(cnt)
