from scipy.stats import ranksums
x = [1.0, 2.0, 3.0, 4.0, 5.0]
y = [2.0, 3.0, 4.0, 5.0, 6.0]
result = ranksums(x=x, y=y, alternative='two-sided')