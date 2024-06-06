import matplotlib.pyplot as plt
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['red', 'green', 'blue', 'yellow']
explode = (0, 0.1, 0, 0)
plt.pie(sizes, colors=colors, labeldistance=1.05, shadow=True, startangle=90, autopct='%1.1f%%', counterclock=False, labels=labels, explode=explode, data=None, radius=False, pctdistance=0.85, normalize=None)