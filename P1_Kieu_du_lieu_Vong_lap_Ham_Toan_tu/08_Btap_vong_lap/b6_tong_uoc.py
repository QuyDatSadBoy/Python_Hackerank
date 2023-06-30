from math import *
if __name__ == '__main__':
    n = int(input())
    sum = 0
    for i in range(1, isqrt(n)+1):
        if (n % i == 0):
            sum += i
            if (i*i != n):
                sum += n//i
    print(sum)
