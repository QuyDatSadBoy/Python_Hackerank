from math import *


def solve(n):
    i = 2
    tam = isqrt(n)
    while i <= tam:
        if (n % i == 0):
            mu = 0
            while (n % i == 0):
                mu += 1
                n //= i
            print(i, mu, sep='^', end='')
            if (n != 1):
                print(" * ", end='')
        i += 1
    if (n > 1):
        print(n, 1, sep='^', end='')


if __name__ == '__main__':
    n = int(input())
    solve(n)
