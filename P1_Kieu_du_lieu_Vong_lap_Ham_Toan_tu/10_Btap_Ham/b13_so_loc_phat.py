from math import *


def check(n):
    n = str(n)
    for i in n:
        if (i != '0' and i != '6' and i != '8'):
            return False
    return True


if __name__ == '__main__':
    n = int(input())
    if (check(n)):
        print(1)
    else:
        print(0)
