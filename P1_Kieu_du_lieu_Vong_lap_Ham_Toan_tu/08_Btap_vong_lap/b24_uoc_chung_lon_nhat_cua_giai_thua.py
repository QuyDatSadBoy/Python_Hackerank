from math import *

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(factorial(min(a, b)))
