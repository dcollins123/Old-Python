# To find the mean, variance, and standard deviation of a discrete random variable, the rv_discrete class must be imported from the scipy.stats library. Next, a list containing the outcomes in a sample space and a list containing the probabilities of each outcome are defined. The outcome and probability lists are then linked.
from scipy.stats import rv_discrete

# Defines a list containing the outcomes in the sample space
x = [0,1,2,3,4,5,6]

# Defines a list containing the probabilities for each outcome
p = [0.1,0.2,0.3,0.1,0.1,0.0,0.2]

# Links the values in x to the probabilities in p
discvar = rv_discrete(values=(x,p))

# To find the mean, the .mean() method is used.
# Returns the mean of the discrete random variable
print(discvar.mean())

# To find the variance, the .var() method is used.
# Returns the variance of the discrete random variable 
print(discvar.var())

# To find the standard deviation, the .std() method is used.
# Returns the standard deviation of the discrete random variable
print(discvar.std())

'''Printed in order:
2.7
3.81
1.95192212959


