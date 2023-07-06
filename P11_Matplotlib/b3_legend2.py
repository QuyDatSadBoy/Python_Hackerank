import matplotlib.pyplot as plt
import numpy as np

year = np.array([2003, 2004, 2005, 2006, 2007, 2008, 2009])
python = np.array([50, 55, 72, 74, 82, 85, 86])
javascript = np.array([60, 70, 30, 80, 80, 80, 80])

plt.plot(year, python, marker="o")
plt.plot(year, javascript, marker="x")
plt.title("moss popular Programming languages")
plt.ylabel("Programming languages")
plt.xlabel("Year")
plt.legend([" Python", "Javascript"], loc="upper left")
plt.show()
