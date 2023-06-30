from math import *
if __name__ == '__main__':
    s = input()
    cnt = 0
    a = ['2', '3', '5', '7']
    for i in s:
        if (i in a) == True:
            cnt += 1
    print(cnt)
