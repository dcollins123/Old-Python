# loads the necessary modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# intialize figure
f, ax = plt.subplots()

# load data frame
crashes = sns.load_dataset("car_crashes")
df = crashes.loc[range(5)]

# plot total crashes
sns.set_color_codes("pastel")
sns.barplot(x="total", y="abbrev", data=df,
            label="Total", color="b")

# plot crashes related to speeding
sns.set_color_codes("muted")
sns.barplot(x="speeding", y="abbrev", data=df,
            label="Speeding-related", color="b")

# title
plt.title('Speeding-related automobile collisions', fontsize=20)

# legend
ax.legend(ncol=1, loc="lower right")
ax.set(xlim=(0, 28), ylabel="State", xlabel="Automobile collisions (per billion miles)");

# saves the image
plt.savefig("stacked.png")