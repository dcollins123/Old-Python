import pandas as pd
nums = [1,2,4,5]
nums_df = pd.DataFrame(nums)
# Prints the summary for each exam
print(nums_df.describe())
print(nums_df.var())

#get 5 summary and variance from numbers quick