import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13])
y = np.array([61, 37, 45, 55, 46, 48, 37, 66, 37, 43, 48, 52, 46, 61])

plt.scatter(x, y)

#calculate equation for trendline
z = np.polyfit(x, y, 1)
p = np.poly1d(z)

#add trendline to plot
plt.plot(x, p(x))

plt.show()

#Scatter plot with trendline for temp in CLE