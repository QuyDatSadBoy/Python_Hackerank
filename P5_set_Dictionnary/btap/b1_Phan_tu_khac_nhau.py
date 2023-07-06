from math import *

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    a = set(a)
    print(len(a))
