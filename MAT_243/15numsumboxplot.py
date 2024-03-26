import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

# reads the mtcars.csv file into a dataframe called mtcars
mtcars = pd.read_csv("https://data-analytics.zybooks.com/mtcars.csv")

# prints the first few lines of mtcars
print(mtcars.head())

#The describe() function gives the five-number summary of the weight of the cars.
print(mtcars.wt.describe())

#In the command above, .wt is needed to display only the summary for the weight. Otherwise, the five-number summaries for each of the attributes or columns are displayed.The command to display the box plot for the weights of the cars as well as the corresponding output are given below.
sns.boxplot(mtcars.wt, width=0.35)

