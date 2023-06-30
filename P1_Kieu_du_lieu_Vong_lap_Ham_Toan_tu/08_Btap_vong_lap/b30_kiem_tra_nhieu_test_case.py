from math import *
if __name__ == '__main__':
    T = int(input())
    while T:
        n = int(input())
        if (n % 2 == 0):
            print("EVEN")
        else:
            print("ODD")
        T -= 1
