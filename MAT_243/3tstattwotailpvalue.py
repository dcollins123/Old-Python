# The scipy.stats.ttest_1samp(a, popmean) function takes in an array or a column of a DataFrame and the hypothesized population mean as inputs and gives the t-statistic and two-tailed p-value as outputs.

import pandas as pd
import scipy.stats as st
scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')
print(st.ttest_1samp(scores['Exam1'], 82))

# Printed: Ttest_1sampResult(statistic=0.53270311028859929, pvalue=0.59664679344599247)
