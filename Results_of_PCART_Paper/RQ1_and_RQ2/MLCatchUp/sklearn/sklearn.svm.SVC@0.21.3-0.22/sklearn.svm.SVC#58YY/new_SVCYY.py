import numpy as np
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
y = np.array([1, 1, 2, 2])
from sklearn.svm import SVC
clf = SVC(1.0, 'rbf', 3, 'auto_deprecated', 0.0, True, False, 0.001, cache_size=200, class_weight=None, break_ties=False)