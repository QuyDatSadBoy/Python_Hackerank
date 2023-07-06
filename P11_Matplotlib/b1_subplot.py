import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(2, 2)
x = np.sort(np.random.randint(1, 100, 50))

# plot
ax[0, 0].plot(x, x)
ax[0, 1].plot(x, x**2)
ax[1, 0].plot(x, x**3)
ax[1, 1].plot(x, np.sqrt(x))

fig.tight_layout()
plt.show()
