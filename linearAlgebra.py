from scipy import linalg
import numpy as np

a = np.array([[1, 2], [4, 5]])
b = linalg.inv(a)
print(b)
