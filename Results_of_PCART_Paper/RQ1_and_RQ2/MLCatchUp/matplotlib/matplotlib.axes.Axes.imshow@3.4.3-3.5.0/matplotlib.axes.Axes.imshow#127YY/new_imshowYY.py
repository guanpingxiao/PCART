import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, cmap='viridis', filterrad=4.0, norm=None, filternorm=True, aspect='auto', interpolation_stage=None)