import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
min_value = np.min(a, axis=None, out=None, keepdims=False, initial=np.inf)
print(min_value)