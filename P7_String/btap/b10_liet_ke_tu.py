from math import *
from collections import Counter

if __name__ == '__main__':
    s = input()
    a = list(Counter(s.split()).items())
    b = a.copy()
    b.sort(key=lambda x: x)
    for i in range(len(b)):
        print(b[i][0], end='')
        if (i != len(b)-1):
            print(' ', end='')
    print()
    for i in range(len(a)):
        print(a[i][0], end='')
        if (i != len(a)-1):
            print(' ', end='')
