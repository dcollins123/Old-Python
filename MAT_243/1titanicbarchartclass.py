# loads the necessary modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# loads the titanic dataset
titanic = sns.load_dataset("titanic")

# sets the style of the bar charts
sns.set(style="whitegrid", color_codes=True)

# title
plt.title('HMS Titanic passengers by class', fontsize=20)

# plots a vertical bar chart
sns.countplot(x="class", color="b", data=titanic);

# saves the image
plt.savefig("verticalbarchart.png")

# shows the image
plt.show()

# plots a horizontal bar chart
sns.countplot(y="class", color="b", data=titanic);