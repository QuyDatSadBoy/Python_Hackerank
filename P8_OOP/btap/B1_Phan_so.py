from math import *


class Ps:
    def __init__(self, tu, mau):
        self.tu = tu
        self.mau = mau

    def toi_Gian(self):
        tam = gcd(self.tu, self.mau)
        self.tu //= tam
        self.mau //= tam

    def __str__(self):
        self.toi_Gian()
        return str(f"{self.tu}/{self.mau}")


if __name__ == "__main__":
    tu, mau = map(int, input().split())
    p = Ps(tu, mau)
    print(p)
