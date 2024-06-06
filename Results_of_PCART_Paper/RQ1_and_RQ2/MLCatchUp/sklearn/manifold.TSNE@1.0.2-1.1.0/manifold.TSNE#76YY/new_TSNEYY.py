import numpy as np
from sklearn.manifold import TSNE
X = np.array([[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]])
X_embedded = TSNE(n_components=2, early_exaggeration=12.0, min_grad_norm=1e-07, learning_rate='warn', n_iter=1000, n_iter_without_progress=300, perplexity=30.0).fit_transform(X, metric_params=None)