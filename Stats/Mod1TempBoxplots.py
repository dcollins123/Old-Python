import random

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

import Mod1TempData

# creates temperature data for Zion. You don't need to know how this data is created. 
# The temperature data created for Zion will be unique to you. 
mean = random.randint(Mod1TempData.temperatures_df['temperature'].min(),
                      Mod1TempData.temperatures_df['temperature'].max())
std_deviation = random.randint(round(Mod1TempData.temperatures_df['temperature'].std(), 0),
                               round(2 * Mod1TempData.temperatures_df['temperature'].std(), 0))
zion_temperatures = np.random.normal(mean, std_deviation, 25)
zion_temperatures = pd.DataFrame(zion_temperatures, columns=['temperature'])

# side-by-side boxplots require the two dataframes to be concatenated and require a
# variable identifying the data
Mod1TempData.temperatures_df['id'] = 'my_data'
zion_temperatures['id'] = 'zion_data'
both_temp_df = pd.concat(Mod1TempData.temperatures_df, zion_temperatures)

# sets a title for the plot, x-axis, and y-axis
plt.title('Boxplot for comparison', fontsize=20)

# prepares the boxplot
sns.boxplot(x="id", y="temperature", data=both_temp_df)

# shows the plot
plt.show()
