from math import *
from collections import Counter

if __name__ == '__main__':
    s = input()
    s = Counter(s)
    t = list(s.items())
    Min, Max = (0, 10**18), (0, 0)
    for i in t:
        if (i[1] > Max[1]):
            Max = i[:]
        else:
            if (i[1] == Max[1]):
                if (i[0] > Max[0]):
                    Max = i[:]
        if (i[1] < Min[1]):
            Min = i[:]
        else:
            if (i[1] == Min[1]):
                if (i[0] > Min[0]):
                    Min = i[:]
    print(Max[0], Max[1])
    print(Min[0], Min[1])
