import pandas as pd
recpts = [3, 37,23,61,36,65,6,24,1,19,72,1,13,40,1]
recpts_df = pd.DataFrame(recpts)
print(recpts_df.describe())

'''Printed:
   0
count  15.000000
mean   26.800000
std    24.355111
min     1.000000
25%     4.500000
50%    23.000000
75%    38.500000
max    72.000000
