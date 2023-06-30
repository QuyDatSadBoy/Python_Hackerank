from math import *

if __name__ == '__main__':
    n = int(input())
    sum = 0
    for i in range(n):
        sum += 1/factorial(i)
    print("%.4f" % sum)
