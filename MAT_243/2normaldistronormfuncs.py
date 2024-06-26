import scipy.stats as st

# For a normal distribution, if the mean is 0 and 
# the standard deviation is 1, what is P(z <= -0.25)?
print(st.norm.cdf(-0.25, 0, 1))

# For a normal distribution, if the mean is 0 and 
# the standard deviation is 1, what is P(z <= 1.5)?
print(st.norm.cdf(1.5, 0, 1))

# For a normal distribution, if the mean is 0 and 
# the standard deviation is 1, what is P(z >= -0.25)?
print(st.norm.sf(-0.25, 0, 1))

# For a normal distribution, if the mean is 0 and 
# the standard deviation is 1, what is P(z >= 1.5)?
print(st.norm.sf(1.5, 0, 1))

# For a normal distribution, if the mean is 0 and 
# the standard deviation is 1, what is P(-0.25 <= z <= 1.5)?
print(st.norm.cdf(1.5, 0, 1) - st.norm.cdf(-0.25, 0, 1))

# For a normal distribution, if the mean is 0 and 
# the standard deviation is 1, what is P(1.5 <= z <= 2.85)?
print(st.norm.cdf(2.85, 0, 1) - st.norm.cdf(1.5, 0, 1))

# For a normal distribution, if the mean is 55 and 
# the standard deviation is 7.5, what is P(x <= 62)?
print(st.norm.cdf(62, 55, 7.5))

# For a normal distribution, if the mean is 55 and 
# the standard deviation is 7.5, what is P(x >= 51)?
print(st.norm.sf(51, 55, 7.5))

# For a normal distribution, if the mean is 55 and 
# the standard deviation is 7.5, what is P(49 <= x <= 60)?
print(st.norm.cdf(60, 55, 7.5) - st.norm.cdf(49, 55, 7.5))

'''Printed:
0.4012936743170763
0.9331927987311419
0.5987063256829237
0.06680720126885807
0.5318991244140656
0.06462123981394485
0.8246760551477705
0.7030985713961488
0.5356520638696805
