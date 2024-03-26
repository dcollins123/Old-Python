#he Height dataset gives the heights, in inches, of students in a particular class. Histograms are plotted using the hist() function in the matplotlib.pyplot library. The function takes the dataset as the first parameter and the number of bins as the optional second parameter.
import pandas as pd
import matplotlib.pyplot as plt
heights = pd.read_csv('http://data-analytics.zybooks.com/height.csv')

fig, ax = plt.subplots()
plt.hist(heights['Height'], bins=6)
ax.set_xlabel('Height')
ax.set_ylabel('Frequency')
plt.savefig('histogram6.png')
plt.show()

#The same data can be represented as a histogram with more bins by modifying the bins argument.
import pandas as pd
import matplotlib.pyplot as plt
heights = pd.read_csv('http://data-analytics.zybooks.com/height.csv')

fig, ax = plt.subplots()
plt.hist(heights['Height'], bins=10)
ax.set_xlabel('Height')
ax.set_ylabel('Frequency')
plt.savefig('histogram10.png')
plt.show()
