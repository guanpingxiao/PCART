from sklearn.svm import SVC
from sklearn.ensemble import BaggingClassifier
from sklearn.datasets import make_classification
(X, y) = make_classification(n_samples=100, n_features=4, n_informative=2, n_redundant=0, random_state=0, shuffle=False)
clf = BaggingClassifier(warm_start=False, random_state=None, oob_score=False, bootstrap_features=False, max_features=1.0, base_estimator=SVC(), n_jobs=None, bootstrap=True, verbose=0, max_samples=1.0).fit(y, base_estimator=X, estimator=None)