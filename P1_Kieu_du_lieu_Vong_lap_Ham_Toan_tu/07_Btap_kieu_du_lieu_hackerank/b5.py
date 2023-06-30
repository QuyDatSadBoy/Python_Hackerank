from math import *
x1, y1, x2, y2 = map(int, input().split())
d = sqrt((x2-x1)**2 + (y2-y1)**2)
print("%.2f" % d)
