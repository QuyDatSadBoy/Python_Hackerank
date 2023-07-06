import numpy as np

# tao arr
arr = np.array([1, 2, 3, 4, 5])
print(type(arr))
arr2 = np.arange(1, 10, 2)
print(arr2)
arr3 = np.linspace(1, 100, 100)
print(arr3)
# tao mang 100 so 0
arr4 = np.ones(10)
arr5 = np.zeros(10)
print(arr4)
print(arr5)
print(arr4.ndim)
print(arr5.shape)
print(arr5.dtype)
print(len(arr))
print(arr.size)

a = np.array([[1, 2, 3], [3, 4, 5], [6, 7, 8]])
subarr = a[0:3, 0:2]
print(subarr)
