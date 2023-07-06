from math import *

if __name__ == '__main__':
    a, b, c = 0, 0, 0
    s = input()
    for i in s:
        if i.isalpha():
            a += 1
        else:
            if i.isdigit():
                b += 1
            else:
                c += 1
    print(a, b, c)
