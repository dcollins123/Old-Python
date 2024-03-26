#The DataFrame.min() function is used to find the minimum, and the DataFrame.max() function is used to find the maximum.
import pandas as pd
scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')

# Prints the minimum score for each exam
print(scores.min())

# Prints the minimum score for Exam1 only
print(scores[['Exam1']].min())

# Prints the maximum score for each exam
print(scores.max())

# Prints the maximum score for Exam1 only
print(scores[['Exam1']].max())


#No pre-built function exists for finding the range. However, the range can be found by subtracting the minimum values from the maximum values. Alternatively, a new function can be defined if the range needs to be found repeatedly.
import pandas as pd
scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')

# Calculating the range by subtracting the minimum from the maximum
score_range = scores.max() - scores.min()
print(score_range)

# Defining a function that can be used repeatedly
def range_of_scores(x):
  return x.max() - x.min()
print(range_of_scores(scores))
print(range_of_scores(scores[['Exam1']]))
print(range_of_scores(scores[['Exam2']]))
print(range_of_scores(scores[['Exam4']]))