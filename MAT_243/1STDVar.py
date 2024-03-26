import pandas as pd

# Loads the ExamScores dataset
scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')

# Prints the standard deviation for each exam
print(scores.std())

# Prints the standard deviation for Exam1 only
print(scores[['Exam1']].std()) 

# Prints the variance for each exam
print(scores.var())

# Prints the variance for Exam1 only
print(scores[['Exam1']].var())

'''Printed:
Exam1     9.291756
Exam2    14.332780
Exam3    21.754296
Exam4     8.056560
dtype: float64
Exam1    9.291756
dtype: float64
Exam1     86.336735
Exam2    205.428571
Exam3    473.249388
Exam4     64.908163
dtype: float64
Exam1    86.336735
dtype: float64

The DataFrame.std() function is used to find the standard deviation, and the DataFrame.var() is used to find the variance.

