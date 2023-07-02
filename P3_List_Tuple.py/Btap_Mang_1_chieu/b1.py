from math import *

if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    cntChan, cntLe, sumChan, sumLe = 0, 0, 0, 0
    for i in a:
        if (i % 2 == 0):
            cntChan += 1
            sumChan += i
        else:
            cntLe += 1
            sumLe += i
    print(cntChan, cntLe, sumChan, sumLe, sep='\n', end='')
