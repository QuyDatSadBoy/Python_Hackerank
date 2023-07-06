from math import *
from collections import Counter

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a = Counter(a)
    b = a.copy()
    a = list(a.items())
    a.sort(key=lambda x: (x[0]))
    for x, y in a:
        print(x, y)
    print()
    for x, y in b.items():
        print(x, y)
