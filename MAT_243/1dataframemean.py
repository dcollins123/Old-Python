import pandas as pd

scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')

# Prints the first few lines of data
print(scores.head())

# Prints the mean for each exam
print(scores.mean())

# Prints the mean for Exam1 only
print(scores[['Exam1']].mean())

# Prints the means for Exam1 and Exam2
print(scores[['Exam1', 'Exam2']].mean())

'''Printed:
 Exam1  Exam2  Exam3  Exam4
0    100     66     74     68
1     76     84    100     75
2     89     80    100     95
3     83     76     91     74
4     86     99     78     78
Exam1    82.70
Exam2    79.40
Exam3    73.34
Exam4    76.50
dtype: float64
Exam1    82.7
dtype: float64
Exam1    82.7
Exam2    79.4
dtype: float64