from sklearn.datasets import make_blobs
(X, y) = make_blobs(n_samples=10, n_features=2, centers=3, cluster_std=1.0, return_centers=False)