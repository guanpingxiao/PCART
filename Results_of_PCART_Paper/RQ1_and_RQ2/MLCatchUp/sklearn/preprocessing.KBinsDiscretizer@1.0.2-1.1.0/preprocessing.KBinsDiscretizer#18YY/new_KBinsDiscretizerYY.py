from sklearn.preprocessing import KBinsDiscretizer
X = [[-2, 1, -4, -1], [-1, 2, -3, -0.5], [0, 3, -2, 0.5], [1, 4, -1, 2]]
est = KBinsDiscretizer(encode='ordinal', strategy='uniform', n_bins=3, dtype=None, subsample='warn', random_state=None)