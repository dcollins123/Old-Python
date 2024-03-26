import pandas as pd

# Create a DataFrame containing the eps data
earnings_surprise = pd.DataFrame([11.36, 7.89, 1.96, 0, -3.12, -9.52])
print(earnings_surprise.mean())
print(earnings_surprise.std())

'''Printed:
0    1.428333
dtype: float64
0    7.526849
dtype: float64

To determine whether the eps of Walmart compared to the other companies is unusual, the sample mean and sample standard deviation should be computed. Using Python, these quantities can be calculated as follows.

