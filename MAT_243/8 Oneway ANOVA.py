#The f_oneway() function performs a one-way ANOVA. The function takes a number of lists of data as parameters, and returns the F-statistic and the P-value. The scipy.stats and statsmodels.formula.api libraries must be imported to use f_oneway().

# The Exam Score dataset includes scores obtained in 4 exams in a class.
# Perform a hypothesis test to determine if the mean scores of the exams 
# are different. Use the 5% level of significance. 

import pandas as pd
import scipy.stats as st
scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')

# Statistics of each exam
exam1_score = scores[['Exam1']]
exam2_score = scores[['Exam2']] 
exam3_score = scores[['Exam3']] 
exam4_score = scores[['Exam4']] 

print(st.f_oneway(exam1_score, exam2_score, exam3_score, exam4_score))
#Printed: F_onewayResult(statistic=array([ 3.85696089]), pvalue=array([ 0.01034867]))

#--------------------------------------------------------------------------------------

#If the data is labeled according to group, ols() can also be used to generate an ANOVA table, which also gives the F-statistic and the corresponding P-value.

import statsmodels.api as sm
import pandas as pd
from statsmodels.formula.api import ols
df = pd.read_csv('http://data-analytics.zybooks.com/ExamScoresGrouped.csv')
mod = ols('Scores ~ Exam',data=df).fit()
aov_table = sm.stats.anova_lm(mod, typ=2)
print(aov_table)

'''Printed:
sum_sq     df         F    PR(>F)
Exam       2400.735    3.0  3.856961  0.010349
Residual  40666.220  196.0       NaN       NaN
'''

#---------------------------------------------------------------------------------------

#Below is the code to generate the box plots for grouped data.

import pandas as pd
import seaborn as sns
df = pd.read_csv('http://data-analytics.zybooks.com/ExamScoresGrouped.csv')
sns.boxplot(x="Exam", y="Scores", data=df)

#---------------------------------------------------------------------------------------
#Or, all together:

# impots the necessary libraries
import statsmodels.api as sm
import pandas as pd
from statsmodels.formula.api import ols
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as st

scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')

# Statistics of each exam
exam1_score = scores[['Exam1']]
exam2_score = scores[['Exam2']] 
exam3_score = scores[['Exam3']] 
exam4_score = scores[['Exam4']] 

print(st.f_oneway(exam1_score, exam2_score, exam3_score, exam4_score))

# loads the data set
df = pd.read_csv('http://data-analytics.zybooks.com/ExamScoresGrouped.csv')

# builds model and produces aov table
mod = ols('Scores ~ Exam',data=df).fit()
aov_table = sm.stats.anova_lm(mod, typ=2)
print(aov_table)

# creates a box plot by exam
sns.boxplot(x="Exam", y="Scores", data=df)
plt.savefig("examscores.png")

#Shows the image
plt.show()