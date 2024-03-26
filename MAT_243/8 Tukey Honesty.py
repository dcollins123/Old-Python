'''The MultipleComparison() function take the data frame column that contains the values and the data frame column that contains the levels as inputs and builds the models. The tukeyhsd() function displays the 95% Tukey's confidence intervals. The statsmodels.stats.multicomp library must be imported to use these functions.'''

import pandas as pd
from statsmodels.stats.multicomp import (pairwise_tukeyhsd, MultiComparison)
df = pd.read_csv('http://data-analytics.zybooks.com/ExamScoresGrouped.csv')
mod = MultiComparison(df['Scores'], df['Exam'])
print(mod.tukeyhsd())

'''Printed: 
Multiple Comparison of Means - Tukey HSD,FWER=0.05
==============================================
group1 group2 meandiff  lower    upper  reject
----------------------------------------------
Exam1  Exam2    -3.3   -10.7652  4.1652 False 
Exam1  Exam3   -9.36   -16.8252 -1.8948  True 
Exam1  Exam4    -6.2   -13.6652  1.2652 False 
Exam2  Exam3   -6.06   -13.5252  1.4052 False 
Exam2  Exam4    -2.9   -10.3652  4.5652 False 
Exam3  Exam4    3.16   -4.3052  10.6252 False 
----------------------------------------------
'''
