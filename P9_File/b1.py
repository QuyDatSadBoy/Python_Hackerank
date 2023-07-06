from math import *


class SV:
    def __init__(self, name, lop):
        self.name = name
        self.lop = lop

    def __str__(self):
        return f"{self.name} {self.lop}"


if __name__ == "__main__":
    fr = open("input.txt", "r")
    fw = open("output.txt", "w")
    d = fr.readlines()
    print(len(d))
    for i in d:
        s = i.split()
        s = (" ".join(s)).title()
        fw.write(s + "\n")
    sv = SV("DAT", "CN06")
    fw.write(str(sv))
    fr.close()
    fw.close()
