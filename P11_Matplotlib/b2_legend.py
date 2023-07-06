import matplotlib.pyplot as plt
import numpy as np

year = np.array([1, 2, 3, 4])
salary = np.array([2, 4, 6, 8])
plt.plot(year, salary, marker="o")
plt.xlabel("Year")
plt.ylabel("Salary")
plt.title("TQD")
plt.legend(["Salary"], loc="upper left")
plt.show()
