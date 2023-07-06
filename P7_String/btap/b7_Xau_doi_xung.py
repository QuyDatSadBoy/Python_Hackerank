from math import *

if __name__ == '__main__':
    s = input()
    if s == s[::-1]:
        print("YES")
    else:
        print("NO")
