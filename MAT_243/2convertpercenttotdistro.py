# The t.ppf() and t.isf() functions are used to convert percentiles to t-statistics. The scipy.stats library must be imported to use these functions.
import scipy.stats as st

# For a t-distribution, if the degrees of freedom is 49, the mean is 0 and 
# the standard deviation is 1, what is t* if P(t < t*) = 0.135?
print(st.t.ppf(0.135, 49, 0, 1))

# For a t-distribution, if the degrees of freedom is 49, the mean is 0 and 
# the standard deviation is 1, what is t* if P(t > t*) = 0.405?
print(st.t.isf(0.405, 49, 0, 1))

# For a t-distribution, if the degrees of freedom is 24, the mean is 55 and 
# the standard deviation is 7.5, what is t* if P(t < t*) = 0.8247?
print(st.t.ppf(0.8247, 24, 55, 7.5))

# For a t-distribution, if the degrees of freedom is 24, the mean is 55 and 
# the standard deviation is 7.5, what is t* if P(t > t*) = 0.95?
print(st.t.isf(0.95, 24, 55, 7.5))

'''Printed:
-1.1156820266358158
0.2417276381058361
62.13980379235694
42.168384400679294