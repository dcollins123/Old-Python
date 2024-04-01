# Pandas dataframe has several methods that calculate descriptive statistics.
import pandas as pd
temperatures = [45, 50, 60, 68, 54, 53, 52, 41, 40, 68, 46, 56, 38, 47]

# prepare a dataframe for temperatures.
temperatures_df = pd.DataFrame(temperatures, columns=['temperature'])
# mean
mean = temperatures_df['temperature'].mean()
print("Mean=", round(mean, 2))

# median
median = temperatures_df['temperature'].median()
print("Median=", round(median, 2))

# variance
variance = temperatures_df['temperature'].var()
print("Variance=", round(variance, 2))

# standard deviation
stdeviation = temperatures_df['temperature'].std()
print("Standard Deviation=", round(stdeviation, 2))

# describe - a useful function that calculates several different descriptive statistics
statistics = temperatures_df['temperature'].describe()
print("")
print("Describe method")
print(statistics)
