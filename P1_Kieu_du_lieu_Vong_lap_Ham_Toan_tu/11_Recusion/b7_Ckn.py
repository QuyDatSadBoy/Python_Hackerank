from math import *


def to_hop(n, k):
    if k == 0 or k == n:
        return 1
    return to_hop(n-1, k)+to_hop(n-1, k-1)


if __name__ == '__main__':
    n, k = map(int, input().split())
    print(to_hop(n, k))
