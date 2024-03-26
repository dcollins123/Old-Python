# loads the seaborn library
import seaborn as sns

# loads the titanic dataset 
titanic = sns.load_dataset("titanic")

#To find the number of rows, the command titanic.shape can be used to find the number of rows and the number of columns. The output is the ordered pair (891, 15) where 891 is the number of rows and 15 is the number of columns.
titanic.shape

#To find the column names, the command titanic.columns is used, which gives the output
titanic.columns

#To find the data types of the columns , the command titanic.dtypes is used, which gives the output
titanic.dtypes

#The code below returns a data frame with only the columns sex and survived from the Titanic data set.
titanic[["sex","survived"]]

#The first 5 rows of the resulting data frame are shown in the output below.
titanic[["sex","survived"]].head()

#To select a row by position, the command data_frame[a:b] where a and b - 1 are the initial and final rows included in the output.
#The code below selects the first 5 rows of the titanic dataset and returns a data frame.
titanic[0:5]

#To select only the rows where one column has a particular value, the command data_frame[data_frame.column == x] is used, where x is the desired value in column.
#The code below selects all the rows where the column pclass has a value of 3.
titanic[titanic.pclass == 3]

#Similarly the comparison operators >, <, >=, <=, can be used to select rows where a column has values more or less than a given value.
#The code below selects all the rows where the column fare has a value less than 10.0.
titanic[titanic.fare < 10.0]

#The loc() is used to select a range of rows and/or a subset of columns. returns a dataframe containing the first 6 rows and the columns pclass and age of the titanic data set as shown below.
titanic.loc[0:5,["pclass","age"]]

#The iloc() is used to select a range of rows and/or columns. returns a DataFrame containing the first 5 rows and the first 5 columns of the titanic data set as shown below.
titanic.iloc[0:5,0:5]

