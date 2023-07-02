from math import *

if __name__ == '__main__':
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if (k in a) == False:
        print("NOT FOUND")
    else:
        a.remove(k)
        for i in a:
            print(i, end=' ')
