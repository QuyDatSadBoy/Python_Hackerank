from math import *
from collections import Counter

if __name__ == '__main__':
    s = input()
    s = Counter(s)
    t = list(s.items())
    t.sort(key=lambda x: x[0])
    for x, y in t:
        print(x, y)
    print()
    for x, y in s.items():
        print(x, y)
