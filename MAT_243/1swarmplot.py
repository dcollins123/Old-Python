# loads the necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# loads the titanic dataset
titanic = sns.load_dataset("titanic")

# title
plt.title('Fares paid by passengers of the Titanic by deck', fontsize=20)

# plot
sns.swarmplot(x="deck", y="fare", hue = "sex", data=titanic);

# saves the image
plt.savefig("titanicswarmplot.png")

# shows the image
plt.show()

'''A swarm plot is created by using the swarmplot function of the seaborn library. An optional parameter hue can also be set to another categorical variable to group each swarm according to the other variable. Ex: The code below displays a swarm plot for the fares paid by passengers by deck where each swarm is grouped by sex.

