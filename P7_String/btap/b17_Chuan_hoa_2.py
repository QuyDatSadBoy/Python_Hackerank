from math import *

if __name__ == "__main__":
    s = input().split()
    res1, res2 = [], []
    for i in range(len(s) - 1):
        if i == len(s) - 2:
            s[i] = s[i] + ","
        res1.append(s[i].title())
    res1.append(s[len(s) - 1].upper())
    s[len(s) - 2] = s[len(s) - 2][0 : len(s[len(s) - 2]) - 1]
    res2.append(s[len(s) - 1].upper() + ",")
    for i in range(0, len(s) - 1):
        res2.append(s[i].title())
    res1 = " ".join(res1)
    res2 = " ".join(res2)
    print(res1, res2, sep="\n")
