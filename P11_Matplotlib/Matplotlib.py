import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4])
y = np.array([5, 6, 7, 7])
plt.plot(y, marker="o")
plt.plot(x, y)
plt.title("TQD")
plt.show()
