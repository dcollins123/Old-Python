import pandas as pd
scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')

# Prints the summary for each exam
print(scores.describe())

# Prints the summary for Exam1 only
print(scores[['Exam1']].describe())

'''The DataFrame.describe() function generates a five-number summary. Q1, the 25th percentile, is shown as 25%, the median, the 50th percentile, is shown as 50%, and Q3, the 75th percentile, is shown as 75%.

Printed:
  Exam1      Exam2       Exam3      Exam4
count   50.000000   50.00000   50.000000   50.00000
mean    82.700000   79.40000   73.340000   76.50000
std      9.291756   14.33278   21.754296    8.05656
min     59.000000   49.00000   18.000000   55.00000
25%     77.250000   68.50000   59.000000   72.00000
50%     83.000000   79.50000   74.500000   75.00000
75%     88.500000   91.75000   94.500000   79.75000
max    100.000000  100.00000  100.000000  100.00000
            Exam1
count   50.000000
mean    82.700000
std      9.291756
min     59.000000
25%     77.250000
50%     83.000000
75%     88.500000
max    100.000000