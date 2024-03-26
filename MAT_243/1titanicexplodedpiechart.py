# data to plot
a = df[df.survived == 1]["survived"].count()
b = df[df.survived == 0]["survived"].count()

# creates a tuple of the categories
explodeTuple = (0.1, 0.0)

# data to plot
labels = 'Survived', 'Did not survive'
sizes = [a, b]

# plot
plt.pie(sizes, labels=labels, autopct='%1.1f%%', explode = explodeTuple)

# title
plt.title('Survivors of the Titanic', fontsize=20)

# produces a perfectly circular chart
plt.axis('equal')

# saves the image
plt.savefig("explodedpiechart.png")

# shows the image
plt.show()

'''o explode one or more categories within a pie chart, the parameter explode of the pie is set to a tuple. Ex: In the tuple (0.1, 0.0), the category "Survived" is exploded by 0.1 units, while the category "Did not survive" is not exploded.