from math import *

if __name__ == "__main__":
    fr = open("input.txt", "r")
    fw = open("output.txt", "w")

    d = fr.read()
    for i in d:
        print(i)
        fw.write(i)

    fr.close()
    fw.close()
