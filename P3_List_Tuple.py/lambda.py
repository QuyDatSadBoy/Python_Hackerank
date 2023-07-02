from math import *

if __name__ == '__main__':
    def func(x, y): return gcd(x, y)
    print(func(10, 20))
    print((lambda x, y: lcm(x, y))(100, 200))
    a = list(range(1, 6))
    b = list(map(lambda x: x**2, a))
    c = list(filter(lambda x: x % 2 == 0, a))
    def find_max(x, y): return x if x > y else y
    print(b)
    print(c)
    print(find_max(100, 200))
