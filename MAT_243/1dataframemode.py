import pandas as pd

# Loads the ExamScores dataset
scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')

# Prints the mode(s) for each exam
print(scores.mode())

# Prints the mode(s) for Exam1 only
print(scores[['Exam1']].mode())

'''Printed:
Exam1  Exam2  Exam3  Exam4
0     78   84.0  100.0   74.0
1     83  100.0    NaN   75.0
2     89    NaN    NaN    NaN
  Exam1
0     78
1     83
2     89

The DataFrame.mode() function is used to find the mode. Multiple modes are shown on separate lines. "NaN" (not a number) is used to fill in blank spaces for columns with fewer modes.

