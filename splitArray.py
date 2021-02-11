import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6])
print(arr)

newarr = np.array_split(arr, 6)
print(newarr)

print(newarr[2])

