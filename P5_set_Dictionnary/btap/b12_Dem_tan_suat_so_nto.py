from math import *
from collections import Counter


def nto(x):
    for i in range(2, isqrt(x)+1):
        if x % i == 0:
            return False
    return x > 1


if __name__ == '__main__':
    a = []
    while True:
        try:
            s = input()
            a.extend(list(map(int, s.split())))
        except EOFError:
            break
    a = list(Counter(a).items())
    a = [x for x in a if nto(x[0])]
    for x, y in a:
        print(x, y)
