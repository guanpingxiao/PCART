import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(sizes, explode, labels, colors, startangle=90, radius=False, autopct='%1.1f%%', pctdistance=0.85, data=None, shadow=True, labeldistance=1.05, normalize=None)
