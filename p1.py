"""
Day 27
(hint: use pandas groupby)
1. Import the necessary libraries
2. Import the dataset(drinks.csv) from common/Python_Exercise folder.
3. Assign it to a variable called drinks.
4. Print the continent that drinks more beer on average?
5. For each continent print the statistics(count,mean,std etc.) for wine consumption.
6. Print the mean alcohol consumption per continent for every column
7. Print the median alcoohol consumption per continent for every column
8. Print the mean, min and max values for spirit consumption.
"""

import pandas as pd
from pandas import Series as s
from pandas import DataFrame as f
drinks = pd.read_csv('drinks.csv')
#print drinks
gp = drinks.groupby('continent')

#4.
print 'Continent that drinks more beer:\n',gp.mean()['beer_servings'].idxmax() #or gp.mean()['beer_servings'].nlargest(1)

#5
print gp.describe()
print gp.agg(['count','mean','std','max','min'])['wine_servings']

#6
print 'MEan----:','\n',gp.mean()
#7
print 'median----:','\n',gp.median() #or gp.agg('median')

#print 'median2-----','\n',gp.agg('median')
#8
print gp.agg(['mean','min','max'])['spirit_servings']
