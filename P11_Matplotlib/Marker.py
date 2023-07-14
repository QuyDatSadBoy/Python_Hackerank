import matplotlib.pyplot as plt
import numpy as np

# moi diem tren do thi duoc danh dau boi marker
# x = np.random.randint(1, 100, 10)
# y = np.random.randint(1, 100, 10)
# plt.plot(x, y, marker="s", ms=12, mfc="hotpink")
# plt.show()
x = np.random.randint(1, 100, 10)
y = np.random.randint(1, 100, 10)
plt.plot(x, y, marker="o", linestyle="dotted", color="r")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()
# plt.subplot(1,2,1) so hang so cot roi den vi tri
# plt.scatter(x,y) thay vi plot de no hien thi rai rac diem
# plt.bar(x,y)
# plt.barh(x,y,width = .8) nam ngang
# plt.pie(y,labels = l)
