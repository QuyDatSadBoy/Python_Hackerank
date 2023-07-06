from math import *
from collections import Counter
from functools import cmp_to_key
from sys import stdin


class Person:
    nationlity = "Viet Nam"

    def __init__(self, name, job, thaydoi):
        nationlity = thaydoi
        self.name = name
        self.job = job

    def greet(self):
        print("xin chao")

    def __str__(self):
        return " ".join([self.name, self.job, self.nationlity])


if __name__ == "__main__":
    p1 = Person("Teo", "Dev", "ok")
    p2 = Person("Ty", "Engineer", "ok")
    print(p1.nationlity, p1.name, p1.job)
    print(p2.nationlity, p2.name, p2.job)
    p1.greet()
    print(p1)
