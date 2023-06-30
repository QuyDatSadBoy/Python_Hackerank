from math import *

if __name__ == '__main__':
    n = int(input())
    sum = 0
    for i in range(1, n+1, 1):
        sum += factorial(i)
    print(sum)
