from math import *

if __name__ == "__main__":
    s = " ".join(input().split()).title()
    ns = input()
    if ns[1] == "/":
        ns = "0" + ns
    if ns[4] == "/":
        ns = ns[0:3] + "0" + ns[3:]
    print(s, ns, sep="\n")
