from math import *
if __name__ == '__main__':
    a = input()
    sum = 0
    for i in a:
        sum += ord(i)-48
    print(sum)
