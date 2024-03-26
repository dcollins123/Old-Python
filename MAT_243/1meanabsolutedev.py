import pandas as pd

# Loads the ExamScores dataset
scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')

# Prints the mean absolute deviation of all scores
print(scores.mad())

# Prints the mean absolute deviation of Exam 1
print(scores['Exam1'].mad())

'''Printed:
Exam1     7.1360
Exam2    12.1200
Exam3    17.7928
Exam4     5.7000
dtype: float64
7.136

The DataFrame.mad() function is used to find the mean absolute deviation.

