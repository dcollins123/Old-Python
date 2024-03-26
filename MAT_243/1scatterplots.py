# loads the necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# creates the data points
x = np.array([0, 5, 3, 4, 7, 8, 10])
y = np.array([5, 2, 5, 15, 27, 15, 31])

# plot
sns.regplot(x, y, ci=None)

# saves the image
plt.savefig("scatterplot.png")

# shows the image
plt.show()

'''To graph a scatter plot, the sns.regplot(x,y, ci = None) function of the seaborn library is used, which takes in two arrays of equal size x and y. By default, the 95% confidence intervals are displayed, but the parameter ci can be set to None to disable confidence intervals.