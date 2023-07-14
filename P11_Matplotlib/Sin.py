import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-50, 50, 1000)
y = np.sin(x)
y2 = np.cos(x)
y3 = -3 / 2 * x * x + 5
plt.plot(x, y3)
plt.title("TQD")
plt.show()

