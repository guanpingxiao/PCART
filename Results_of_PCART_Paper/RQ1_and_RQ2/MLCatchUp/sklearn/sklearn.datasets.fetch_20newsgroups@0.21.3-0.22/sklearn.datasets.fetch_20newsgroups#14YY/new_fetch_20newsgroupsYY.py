from sklearn.datasets import fetch_20newsgroups
newsgroups_train = fetch_20newsgroups(None, subset='train', categories=None, shuffle=True, return_X_y=False)