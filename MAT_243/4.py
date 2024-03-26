'''
The ztest(x1, x2, value = 0) function can also be used to perform a two-sample z-test for means. However, the value parameter should be set to 0. The function requires the statsmodels.stats.weightstats library to be imported and takes two inputs. The first input x1 is an array containing sample observations from one population and the second input is also an array containing sample observations from another population.

The function returns the z-score and the two-tailed p-value.
'''

from statsmodels.stats.weightstats import ztest
sample1 = [21, 28, 40, 55, 58, 60]
sample2 = [13, 29, 50, 55, 71, 90]
print(ztest(x1 = sample1, x2 = sample2))

# Printed: (-0.58017208108908169, 0.56179857900464247)

# ----------------------------------------------------------------------------------

# The st.ttest_rel(x, y) function takes two arrays or DataFrame columns x and y with the same length as inputs and returns the t-statistic and the corresponding two-tailed p-value as outputs.

import scipy.stats as st
import pandas as pd
df = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')
st.ttest_rel(df['Exam1'],df['Exam2'])

# Printed: Ttest_relResult(statistic=1.4179252582484649, pvalue=0.16254101610053867)

# ---------------------------------------------------------------------------------
#The Caffeine dataset uses data from "The Effect of Different Dosages of Caffeine on Endurance Performance Time", International Journal of Sports Medicine1 and gives the endurance times (in minutes) of 9 athletes when given a caffeine dose of 5 milligrams and 13 milligrams.

import scipy.stats as st
import pandas as pd
df = pd.read_csv('http://data-analytics.zybooks.com/Caffeine.csv')
st.ttest_rel(df['mg5'],df['mg13'])

# Printed: Ttest_relResult(statistic=-0.12052261484527026, pvalue=0.90704115640761218)

# ----------------------------------------------------------------------------------------

# The st.ttest_ind(x, y) command takes two arrays or DataFrame columns x and y with the same length as inputs and returns the t-statistic and the corresponding two-tailed p-value as outputs.

import scipy.stats as st
import pandas as pd
df = pd.read_csv('http://data-analytics.zybooks.com/Machine.csv')
st.ttest_ind(df['Old'],df['New'])

# Printed: Ttest_indResult(statistic=3.397230706117603, pvalue=0.0032422494663179747)

# ----------------------------------------------------------------------------------------

import scipy.stats as st
import pandas as pd
df = pd.read_csv('http://data-analytics.zybooks.com/Memory.csv')
st.ttest_ind(df['nodrug'], df['drug'], equal_var=False)

# ---------------------------------------------------------------------------------------
'''The proportions_ztest() function can also perform a z-test between two samples. The function requires the statsmodels.stats.proportion library to be imported, and takes two arrays, instead of two integers, as parameters. The first array is the number of individuals meeting some condition in each group, and the second array is the total number of individuals in each group.

The function returns the z-score and the two-tailed p-value.
'''
from statsmodels.stats.proportion import proportions_ztest
counts = [95, 125]
n = [5000, 5000]
print(proportions_ztest(counts, n))

# Printed: (-2.0452221470506315, 0.040832962004731133)

