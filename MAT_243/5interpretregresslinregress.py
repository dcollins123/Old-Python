import pandas as pd
import scipy.stats as st
df = pd.read_csv('http://data-analytics.zybooks.com/Reaction.csv') 
print(st.linregress(df['Drinks'],df['Reaction']))

'''Printed:
LinregressResult(slope=6.0000000000000009, intercept=3.9999999999999964,
 rvalue=0.97281665268828232, pvalue=0.0010983582017795293, stderr=0.71414284285428509)
 
'''
