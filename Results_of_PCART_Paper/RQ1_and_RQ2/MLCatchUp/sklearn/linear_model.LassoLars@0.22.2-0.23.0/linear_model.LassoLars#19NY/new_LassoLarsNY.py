from sklearn import linear_model
reg = linear_model.LassoLars(1.0, verbose=False, normalize=True, precompute='auto', fit_intercept=True, jitter=None, random_state=None)