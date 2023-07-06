from math import *
from collections import Counter


def so_Ko_Giam(x):
    s = str(x)
    for i in range(0, len(s)-1):
        if s[i] > s[i+1]:
            return False
    return True


if __name__ == '__main__':
    a = []
    while True:
        try:
            s = input()
            a += map(int, s.split())
        except EOFError:
            break
    a = list(Counter(a).items())
    a = [x for x in a if so_Ko_Giam(x[0])]
    a.sort(key=lambda x: (-x[1], x[0]))
    for x, y in a:
        print(x, y)
