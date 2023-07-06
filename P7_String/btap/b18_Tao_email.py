from math import *

if __name__ == "__main__":
    n = int(input())
    while n:
        s = (input().lower()).split()
        res = s[-2]
        for i in range(len(s) - 2):
            res += s[i][0]
        res += "@xyz.edu.vn"
        print(res)
        ans = s[-1].split("/")
        for i in range(len(ans)):
            print(int(ans[i]), end="")
        print()
        n -= 1
