from sklearn.metrics import explained_variance_score
y_true = [3, -0.5, 2, 7]
y_pred = [2.5, 0.0, 2, 8]
explained_variance_score(y_pred=y_pred, multioutput='uniform_average', y_true=y_true, sample_weight=None, force_finite=True)
