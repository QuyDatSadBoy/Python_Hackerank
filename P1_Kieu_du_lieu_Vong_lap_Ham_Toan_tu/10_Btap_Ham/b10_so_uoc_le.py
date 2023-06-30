from math import *
if __name__ == "__main__":
    n = int(input())
    tam = isqrt(n)
    if (tam*tam == n):
        print("YES")
    else:
        print("NO")
