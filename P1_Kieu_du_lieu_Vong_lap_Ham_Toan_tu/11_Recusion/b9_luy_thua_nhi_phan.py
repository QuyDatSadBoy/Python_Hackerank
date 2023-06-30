from math import *


def pow_mod(a, b):
    if (b == 0):
        return 1
    res = pow_mod(a, b//2) % int(1e9+7)
    res = (res*res) % int(1e9+7)
    if (b % 2 == 1):
        res = ((res % int(1e9+7)) * (a % int(1e9+7))) % int(1e9+7)
    return res


if __name__ == "__main__":
    a, b = map(int, input().split())
    print(pow_mod(a, b))
