from math import *


def solve(n):
    for i in range(2, isqrt(n)+1):
        if (n % i == 0):
            ans = i
            while (n % i == 0):
                n //= i
    if (n > 1):
        ans = n
    print(ans)


if __name__ == '__main__':
    T = int(input())
    while T > 0:
        n = int(input())
        solve(n)
        T -= 1
