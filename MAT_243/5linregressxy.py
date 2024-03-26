# The numpy library is imported to build two arrays
import numpy as np
import scipy.stats as st

x = np.array([0, 3, 7, 10])
y = np.array([5, 5, 27, 31])

print(st.linregress(x,y))

# Printed: LinregressResult(slope=3.0, intercept=2.0, rvalue=0.94542880030087728, pvalue=0.054571199699122705, stderr=0.73108327748669655)


'''The intercept parameter estimator b-sub0 and the slope parameter estimator b-sub1 can be obtained by using the linregress(x,y) function, which takes in two arrays of equal length as input and returns b-sub0, b-sub1, the correlation coefficient r, the p-value for the correlation coefficient t-test, and the corresponding standard error. The linregress(x,y) function uses the scipy.stats library.