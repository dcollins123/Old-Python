df = pd.DataFrame({'Student': {0: "Michael", 1: "Arushi", 2: "Roberta"},
...                    'SAT': {0: 1480, 1: 1520, 2: 1460}, 
...                    'ACT': {0: 34, 1: 32, 2: 32}}, 
...                     columns=['Student','SAT','ACT'])

pd.melt(df, id_vars = "Student", var_name = "Test", value_vars = ["SAT", "ACT"], value_name = "Scores")

'''Printed:
Wide Form:
Student   SAT  ACT
0  Michael  1480   34
1   Arushi  1520   32
2  Roberta  1460   32

after melt, long form:
Student Test  Scores
0  Michael  SAT    1480
1   Arushi  SAT    1520
2  Roberta  SAT    1460
3  Michael  ACT      34
4   Arushi  ACT      32
5  Roberta  ACT      32