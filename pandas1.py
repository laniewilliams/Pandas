import pandas as pd

grades = pd.Series([87,100,94])

print(grades)

a = pd.Series(98.6, range(3))

print()

b = grades[0]
c = grades.count()
d = grades.mean()

print(grades.describe()) #gets statistical information in one shot

grades = pd.Series([87,100,94], index=['Wally','Eva','Sam'])

#print(grades)

grades_dict = {'wally':87,'Eva':100,'Sam': 94}

grades_ds = pd.Series(grades_dict) #the keys in the dictionary become the indexes and the values are the columns in the data series

print(grades_ds)

eva = grades['Eva']

wally = grades.Wally #dot notation only works for STRING indexes

print()
