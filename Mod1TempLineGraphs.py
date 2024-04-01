import matplotlib.pyplot as plt
import pandas as pd

temperatures = [45, 50, 60, 68, 54, 53, 52, 41, 40, 68, 46, 56, 38, 47]

# prepare a dataframe for temperatures.
temperatures_df = pd.DataFrame(temperatures, columns=['temperature'])
# line chart
plt.plot(temperatures_df['temperature'])  # plot

# setting a title for the plot, x-axis and y-axis
plt.title('Line plot of temperature data', fontsize=20) 
plt.xlabel('day')
plt.ylabel('temperature')

# show the plot
plt.show()
