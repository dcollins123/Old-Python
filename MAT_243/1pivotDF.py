# Creates a data frame
df = pd.DataFrame({
...                     
...                    'Student': {0: "Michael", 1: "Arushi", 2: "Roberta", 
...                     3: "Michael", 4: "Arushi", 5: "Roberta"},
...                    'Score': {0: 90, 1: 98, 2: 92, 3: 90, 4: 98, 5: 92}, 
...                    'Date': {0: "2018-01-03", 1: "2018-01-03", 2: "2018-01-03", 3: "2018-01-13", 
...                     4: "2018-01-13", 5: "2018-01-13"}}, 
...                     columns=['Date','Student','Score'])

pd.pivot(df, index = "Date", columns = "Student", values= "Score")

'''Printed:
Long form:
Date  Student  Score
0  2018-01-03  Michael     90
1  2018-01-03   Arushi     98
2  2018-01-03  Roberta     92
3  2018-01-13  Michael     90
4  2018-01-13   Arushi     98
5  2018-01-13  Roberta     92

Wide Form:
Student     Arushi  Michael  Roberta
Date                                
2018-01-03      98       90       92
2018-01-13      98       90       92

The index labels of the pivoted data frame are the unique values of the column Date. The columns of the pivoted data frame are the unique values of the column Student. The values of the pivoted data frame are the values from the column Score.

The code to generate the data frame in long form and the corresponding output are given below.