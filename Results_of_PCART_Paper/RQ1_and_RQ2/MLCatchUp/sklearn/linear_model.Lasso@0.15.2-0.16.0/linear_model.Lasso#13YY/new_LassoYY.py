from sklearn import linear_model
clf = linear_model.Lasso(1.0, True, normalize=False, precompute='auto', random_state=None, selection='cyclic')
