#The chisquare object from the scipy.stats library can be used to perform a chi-square goodness of fit test. Ex: a biologist is counting birds on the lake and comparing the distribution to last week's counts. The observed and expected counts are given in the table below.

from scipy.stats import chisquare

# Calculates the chi-square statistic and $p$-value for alpha = 0.05 for the given observed and expected counts
statistic, pvalue = chisquare([61, 17, 11, 15, 6], f_exp=[55, 25.3, 13.2, 11, 5.5])

print(statistic)
print(pvalue)

''' Printed: 
5.244137022397893
0.26315206062015767

chisquare thus returns the same results as calculated in the example above.
'''

#------------------------------------------------------------------------------------

'''
The chi2_contingency object from the scipy.stats library can be used to perform a chi-square goodness of fit test. Conducting the chi-square test for independence requires first constructing a contingency table. An example using the parole data is shown below. Is there an association between a punishment record while in prison and success or failure while in prison?
'''

import numpy as np
from scipy.stats import chi2_contingency

# Construct a contingency table
parole = np.array([[405,1422], [240,470], [151,275]])

#The command for the chi-square test and corresponding output are displayed below.

# Calculate the test statistic, $p$-value, degrees of freedom, and expected counts
chi2, p, df, ex = chi2_contingency(parole)
print(chi2)
print(p)
print(df)
print(ex)

'''Printed:
53.87860692066112
1.9971429926442894e-12
2
[[ 490.81741478 1336.18258522]
 [ 190.73911576  519.26088424]
 [ 114.44346946  311.55653054]]
'''
 #----------------------------------------------------------------------------------------

#People's preference for beer versus wine are recorded in three cities. Based on the expected values and chi-square test results given below, does drink preference vary among cities?

z = np.array([[2039.122, 509.7804, 5.097804], [1920.878, 450.2196, 4.902196]])

chi2, p, df, ex = chi2_contingency(z)
print(chi2)
print(p)
print(df)
print(ex)

'''Printed:
0.80409
0.66895
2
[[2051.48900768  497.33066853    5.1805278 ]
 [1908.51099232  462.66933147    4.8194722 ]]
 '''

#----------------------------------------------------------------------------------------

#The chi-square test statistic is the same as for the test for independence.

z = np.array([[551, 580], [244, 289], [387, 503], [452, 618], [443,742]])

chi2, p = chi2_contingency(z)
print(chi2)
print(p)

'''Printed:
32.2443
1.70526e-6
'''
