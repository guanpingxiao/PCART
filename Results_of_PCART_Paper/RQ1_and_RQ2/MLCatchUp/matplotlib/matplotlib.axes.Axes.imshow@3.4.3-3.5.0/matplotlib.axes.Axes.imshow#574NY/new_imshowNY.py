import matplotlib.pyplot as plt
import numpy as np
X = np.random.rand(100, 100)
plt.imshow(X, 'viridis', None, origin='upper', vmax=None, resample=None, extent=None, aspect='auto', interpolation='nearest', alpha=None, vmin=None, interpolation_stage=None)