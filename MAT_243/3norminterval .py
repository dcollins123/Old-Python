# The norm.interval() function is used to find a confidence interval for a normally distributed variable. The function takes the desired confidence level, the sample mean, and the standard error as parameters.
import scipy.stats as st
print(st.norm.interval(0.95, 0, 1))
# Printed: (-1.959963984540054, 1.959963984540054)

# A confidence interval can also be calculated from raw data. The following example imports data from ExamScores.csv into a DataFrame, calculates the sample mean, calculates the standard error based on a given population standard deviation, and calculates the 99% confidence interval.
scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')
sigma = 2.5
mean = scores['Exam1'].mean()
stderr = sigma/math.sqrt(len(scores['Exam1']))
print(st.norm.interval(0.99, mean, stderr))
# Printed: (81.78930681614078, 83.610693183859226)
