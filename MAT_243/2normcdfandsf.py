# norm.cdf(z, mean, sd) returns the probability of z being less or equal to than the critical value z for a normal distribution with the specified mean and standard deviation.
import scipy.stats as st

# For a normal distribution, if the mean is 0 and 
# the standard deviation is 1, what is P(z <= -0.25)?
print(st.norm.cdf(-0.25, 0, 1))

# For a normal distribution, if the mean is 0 and 
# the standard deviation is 1, what is P(z <= 1.5)?
print(st.norm.cdf(1.5, 0, 1))
# Printed: 0.401293674317
#          0.933192798731

# norm.sf(z, mean, sd) returns the probability of z being greater than or equal to the critical value z for a normal distribution with the specified mean and standard deviation.
# For a normal distribution, if the mean is 0 and 
# the standard deviation is 1, what is P(z >= -0.25)?
print(st.norm.sf(-0.25, 0, 1))

# For a normal distribution, if the mean is 0 and 
# the standard deviation is 1, what is P(z >= 1.5)?
print(st.norm.sf(1.5, 0, 1))
# Printed: 0.531899124414
#          0.0646212398139
 
# Both norm.cdf() and norm.sf() can also be used for non-standard normal distributions, that is, when the mean is not 0 or the standard deviation is not 1.
# For a normal distribution, if the mean is 55 and 
# the standard deviation is 7.5, what is P(x <= 62)?
print(st.norm.cdf(62, 55, 7.5))

# For a normal distribution, if the mean is 55 and 
# the standard deviation is 7.5, what is P(x >= 51)?
print(st.norm.sf(51, 55, 7.5))

# For a normal distribution, if the mean is 55 and 
# the standard deviation is 7.5, what is P(49 <= x <= 60)?
print(st.norm.cdf(60, 55, 7.5) - st.norm.cdf(49, 55, 7.5))
''' Printed: 0.824676055148
             0.703098571396
             0.53565206387

