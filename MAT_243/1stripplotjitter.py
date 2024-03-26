# loads the necessary libraries
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# loads the titanic dataset
titanic = sns.load_dataset("titanic")

# title
plt.title('Fares paid by passengers of the Titanic by deck', fontsize=20)

# plot
sns.stripplot(x="deck", y="fare", data=titanic);

# saves the image
plt.savefig("titanicstripplot.png")

# shows the image
plt.show()

'''A strip plot is created by using the sns.stripplot function of the seaborn library. Ex: The code below creates a strip plot where the horizontal axis is the deck to which a passenger of the Titanic is assigned and the vertical axis is the fare paid in dollars.

To add jittering to a strip plot, the parameter jitter should be set to true as shown below.
'''
sns.stripplot(x="deck", y="fare", jitter= True, data=titanic);
