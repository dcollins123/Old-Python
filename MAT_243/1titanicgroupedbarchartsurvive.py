# loads the necessary modules
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# loads the titanic dataset
titanic = pd.read_csv("https://static-resources.zybooks.com/static/titanic.csv")

# sets the style of the bar charts
sns.set(style="whitegrid", color_codes=TRUE)

# title
plt.title('Titanic survivors and deaths by class', fontsize=20)

# generates a vertical bar chart
sns.countplot(x="class", hue="survived", color="b", data=titanic);

# saves the image
plt.savefig("groupedbarchart.png")

# shows the image
plt.show()