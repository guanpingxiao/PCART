from sklearn import linear_model
clf = linear_model.ElasticNet(alpha=1.0, l1_ratio=0.5, fit_intercept=True, random_state=None, selection='cyclic')