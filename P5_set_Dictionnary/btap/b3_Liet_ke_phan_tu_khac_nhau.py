from math import *
from collections import Counter

if __name__ == '__main__':
    n = int(input())
    a = list(Counter(map(int, input().split())).items())
    a = [x[0] for x in a]
    for i in a:
        print(i, end=' ')
