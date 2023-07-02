from math import *
from collections import Counter

if __name__ == '__main__':
    a = ['name', 'job', 'address']
    print(a.count('address'))
    b = ['TQD', 'Dev', 'Hn']
    c = dict(zip(a, b))
    print(c)
    d = dict.fromkeys(a, 0)
    print(d)
    e = [1, 1, 2, 2, 2, 3, 3, 4, 5]
    f = list(Counter(e).items())
    f.sort(key=lambda x: (-x[1], -x[0]))
    print(f)
