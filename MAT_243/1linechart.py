# imports the necessary modules
import pandas as pd
import matplotlib.pyplot as plt

# loads the unemployment dataset
unemployment = pd.read_csv('http://data-analytics.zybooks.com/unemployment.csv')

# title
plt.title('U.S. unemployment rate', fontsize = 20)

# x and y axis labels
plt.xlabel('Year')
plt.ylabel('% of total labor force')

# plot
plt.plot(unemployment["Year"], unemployment["Value"])

# saves the image
plt.savefig("linechart.png")

# shows the image
plt.show()

#The code below loads the dataset containing unemployment rates in the United States from 1980 to 2017 and plots the data as a line chart.

