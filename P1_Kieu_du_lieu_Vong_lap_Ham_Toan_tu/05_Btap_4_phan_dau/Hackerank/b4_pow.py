import math
a, b = map(int, input().split())
res = pow(a, b)
if res == int(res):
    print(int(res))
else:
    print('%.2f' % res)
