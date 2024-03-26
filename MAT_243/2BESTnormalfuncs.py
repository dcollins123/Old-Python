import scipy.stats as st

# For a normal distribution, if the mean is 0 and 
# the standard deviation is 1, what is z* if P(z < z*) = 0.135?
print(st.norm.ppf(0.135, 0, 1))

# For a normal distribution, if the mean is 0 and 
# the standard deviation is 1, what is z* if P(z > z*) = 0.405?
print(st.norm.isf(0.405, 0, 1))

# For a normal distribution, if the mean is 55 and 
# the standard deviation is 7.5, what is x* if P(x < x*) = 0.8247?
print(st.norm.ppf(0.8247, 55, 7.5))

# For a normal distribution, if the mean is 55 and 
# the standard deviation is 7.5, what is x* if P(x > x*) = 0.95?
print(st.norm.isf(0.95, 55, 7.5))

'''Printed:
-1.1030625561995975
0.2404260311423079
62.00069589151078
42.66359779786396

The norm.ppf() and norm.isf() functions are used to convert percentiles to z-scores. The scipy.stats library must be imported to use these functions.