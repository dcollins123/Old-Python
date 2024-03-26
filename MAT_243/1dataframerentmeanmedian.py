#The rent dataset lists the monthly rent (in USD) of 10 apartments with area less than 1000ft2 in 6 cities. The columns of the dataset give the rents in Santa Monica, CA, Boise, ID, Tucson, AZ, Detroit, MI, Pittsburgh, PA, and Orlando, FL.
#To find the mean and median, the CSV file is first imported into Python as a pandas DataFrame.
import pandas as pd
rent = pd.read_csv('http://data-analytics.zybooks.com/rent.csv')
print(rent)

#The mean rent for Santa Monica is found as follows.
print(rent['Santa Monica CA'].mean())

#The mean rent for all cities is found as follows.
print(rent.mean())

#The median rent for all cities is found as follows.
print(rent.median())

'''Printed in order:
Santa Monica CA  Boise ID  Tucson AZ  Detroit MI  Pittsburgh PA  Orlando FL
0            10230      1600       2495        3195           2480        2242
1            10000      1500       2200        2695           2435        2000
2             9000      1029       2150        2595           2405        1912
3             8500      1025       1800        2495           2350        1895
4             8250       980       1650        2495           2320        1800
5             8000       950       1600        1675           2316        1765
6             7000       950       1500        1525           2305        1685
7             6500       925       1500        1480           2290        1670
8             6000       925       1500        1410           2275        1665
9             5815       900       1500        1400           2265        1625

7929.5

Santa Monica CA    7929.5
Boise ID           1078.4
Tucson AZ          1789.5
Detroit MI         2096.5
Pittsburgh PA      2344.1
Orlando FL         1825.9
dtype: float64

Santa Monica CA    8125.0
Boise ID            965.0
Tucson AZ          1625.0
Detroit MI         2085.0
Pittsburgh PA      2318.0
Orlando FL         1782.5
dtype: float64
