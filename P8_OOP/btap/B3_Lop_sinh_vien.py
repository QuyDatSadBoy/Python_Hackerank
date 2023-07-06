from math import *


class Sv:
    ma = "SV001"

    def __init__(self, ten, lop, ns, diem):
        self.ten = ten
        self.lop = lop
        self.ns = ns
        self.diem = diem

    def chuanHoa(self):
        ns = self.ns
        if ns[1] == "/":
            ns = "0" + ns
        if ns[4] == "/":
            ns = ns[0:3] + "0" + ns[3:]
        self.ns = ns

    def __str__(self):
        self.chuanHoa()
        return f"{self.ma} {self.ten} {self.lop} {self.ns} {self.diem:.1f}"


if __name__ == "__main__":
    sv = Sv(input(), input(), input(), float(input()))
    print(sv)
