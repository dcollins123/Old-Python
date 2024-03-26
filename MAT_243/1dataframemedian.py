import pandas as pd

# Loads the ExamScores dataset
scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')

# Prints the median for each exam
print(scores.median())

# Prints the median for Exam1 only
print(scores[['Exam1']].median())

'''Printed:
Exam1    83.0
Exam2    79.5
Exam3    74.5
Exam4    75.0
dtype: float64
Exam1    83.0
dtype: float64