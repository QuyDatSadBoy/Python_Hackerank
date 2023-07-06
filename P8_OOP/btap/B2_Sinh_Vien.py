from math import *


class Sv:
    def __init__(self, name, ns, f1, f2, f3):
        self.name = name
        self.ns = ns
        self.f1 = f1
        self.f2 = f2
        self.f3 = f3

    def getTong(self):
        return self.f1 + self.f2 + self.f3

    def __str__(self):
        return f"{self.name} {self.ns} {self.getTong():.1f}"


if __name__ == "__main__":
    sv = Sv(input(), input(), float(input()), float(input()), float(input()))
    print(sv)
