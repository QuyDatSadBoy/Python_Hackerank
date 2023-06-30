from math import *
if __name__ == '__main__':
    n = int(input())
    if (n < 2):
        print(-1)
    else:
        y = 0
        x = 0
        # 2x + 3y = n
        for i in range(0, n//3+1):
            if ((n-3*i) % 2 == 0):
                y = i
                x = (n-3*i)//2
                break
        print(x+y)
        for i in range(x):
            print(2, end=' ')
        for i in range(y):
            print(3, end=' ')
