import pandas as pd
nums = [61, 37, 45, 55, 46, 48, 37, 66, 37, 43, 48, 52, 46, 61]
nums_df = pd.DataFrame(nums)
# Prints the summary for each exam
print(nums_df.describe())
print('Mode:', nums_df.mode())
print('Variance:', nums_df.var())
print('Median:', nums_df.median())

# df quicky