#The rent dataset is first imported.
import pandas as pd
rent = pd.read_csv('http://data-analytics.zybooks.com/rent.csv')
print(rent)

#The maximum and minimum rent for all cities are found as follows.
print(rent.max())
print(rent.min())

#The range in rent for all cities is found by subtracting the minimum rents from the maximum rents.
print(rent.max() - rent.min())

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

Santa Monica CA    10230
Boise ID            1600
Tucson AZ           2495
Detroit MI          3195
Pittsburgh PA       2480
Orlando FL          2242
dtype: int64
Santa Monica CA    5815
Boise ID            900
Tucson AZ          1500
Detroit MI         1400
Pittsburgh PA      2265
Orlando FL         1625
dtype: int64

Santa Monica CA    4415
Boise ID            700
Tucson AZ           995
Detroit MI         1795
Pittsburgh PA       215
Orlando FL          617
dtype: int64