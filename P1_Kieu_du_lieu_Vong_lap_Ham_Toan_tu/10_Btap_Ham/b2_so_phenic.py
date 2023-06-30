from math import *


def check(n):
    cnt = 0
    i = 2
    while i <= isqrt(n):
        if (n % i == 0):
            cnt += 1
            mu = 0
            while (n % i) == 0:
                n //= i
                mu += 1
                if (mu >= 2):
                    return False
                if (cnt >= 3):
                    return False
        i += 1
    if (n != 1):
        cnt += 1
    return cnt == 3


if __name__ == '__main__':
    a = int(input())
    if (check(a)):
        print(1)
    else:
        print(0)
