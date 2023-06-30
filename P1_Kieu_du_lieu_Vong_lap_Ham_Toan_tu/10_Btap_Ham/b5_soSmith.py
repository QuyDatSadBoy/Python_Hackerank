from math import *


def tong(n):
    n = str(n)
    sum = 0
    for i in n:
        sum += ord(i)-48
    return sum


def smith(n):
    sum1 = tong(n)
    sum2 = 0
    tam = n
    for i in range(2, isqrt(n)+1):
        if (n % i == 0):
            while (n % i == 0):
                sum2 += tong(i)
                n //= i
    if (n == tam):
        return False
    if (n > 1):
        sum2 += tong(n)
    return sum1 == sum2


if __name__ == '__main__':
    n = int(input())
    if (smith(n)):
        print("YES")
    else:
        print("NO")
