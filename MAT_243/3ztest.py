# The ztest(x1, value) function is used to perform a one-sample z-test for means. The function requires the statsmodels.stats.weightstats library to be imported, and takes two inputs. The first input x1 is an array and the second input value is the hypothesized value of the population mean. The function returns the z-score and the two-tailed p-value.

from statsmodels.stats.weightstats import ztest
import pandas as pd
scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')
print(ztest(x1 = scores['Exam1'],  value = 86))

# Printed: (-2.5113146627890988, 0.012028242796839027)
