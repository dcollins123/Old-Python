'''The ols() function performs ordinary linear regression, and the fit() function fits the data to the regression line. These functions require the statsmodels.formula.api library to be imported. ols() takes two parameters. The first parameter is in the form 'Y ~ X', where Y is the response variable and X is the predictor variable. The second parameter is the dataset that contains the variables.

The summary() function returns a summary including estimates for the parameters,t-statistics, p-values, and confidence intervals.

All of the above functions require the statsmodels.formula.api library to be imported.'''

import pandas as pd
import statsmodels.formula.api as smf
scores = pd.read_csv('http://data-analytics.zybooks.com/ExamScores.csv')

model = smf.ols('Exam4 ~ Exam2', scores).fit()
print(model.summary())

'''Printed:
OLS Regression Results                            
==============================================================================
Dep. Variable:                  Exam4   R-squared:                       0.101
Model:                            OLS   Adj. R-squared:                  0.082
Method:                 Least Squares   F-statistic:                     5.405
Date:                Wed, 25 Oct 2017   Prob (F-statistic):             0.0244
Time:                        21:59:27   Log-Likelihood:                -172.10
No. Observations:                  50   AIC:                             348.2
Df Residuals:                      48   BIC:                             352.0
Df Model:                           1                                         
Covariance Type:            nonrobust                                         
==============================================================================
                 coef    std err          t      P>|t|      [0.025      0.975]
------------------------------------------------------------------------------
Intercept     62.3017      6.204     10.042      0.000      49.828      74.776
Exam2          0.1788      0.077      2.325      0.024       0.024       0.333
==============================================================================
Omnibus:                        4.604   Durbin-Watson:                   1.676
Prob(Omnibus):                  0.100   Jarque-Bera (JB):                3.507
Skew:                           0.509   Prob(JB):                        0.173
Kurtosis:                       3.805   Cond. No.                         459.
==============================================================================
'''
#---------------------------------------------------------------------------------
'''The ols() function takes two parameters, 'Y ~ X1' where Y is the response variable and X1 is a predictor variable, and a data frame. The sm.stats.anova_lm command takes in a linear model and an ANOVA type as parameters and outputs an ANOVA table. The different types of ANOVA are beyond the scope of this material. To give the correct output, the parameter for the ANOVA type, denoted as typ, is set to 2.
In the code below, Exam4 is the response variable and Exam1 is the predictor variable.'''

from statsmodels.formula.api import ols
import statsmodels.api as sm
import pandas as pd
df=pd.read_csv("http://data-analytics.zybooks.com/ExamScores.csv")
mod = ols('Exam4 ~ Exam1',df).fit()
print(sm.stats.anova_lm(mod, typ=2))

'''Printed:
 sum_sq    df         F    PR(>F)
Exam1      217.166351   1.0  3.517655  0.066808
Residual  2963.333649  48.0       NaN       NaN
'''