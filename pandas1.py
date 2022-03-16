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

grades_dict = {'Wally':87,'Eva':100,'Sam': 94}

grades_ds = pd.Series(grades_dict) #the keys in the dictionary become the indexes and the values are the columns in the data series

print(grades_ds)

eva = grades['Eva']

wally = grades.Wally #dot notation only works for STRING indexes

e = grades.values





hardware = pd.Series(['Hammer','Saw','Wrench'])

f = hardware.str.contains('a')

g = hardware.str.upper()

#convert a series object to a Python list

hardware_list = hardware.to_list()

ds1 = pd.Series([2,4,6,8,10])
ds2 = pd.Series([1,3,5,7,10])

ds1 == ds2

ds1 > ds2

ds1 < ds2

#Convert a series of lists to one series

list_of_series = pd.Series([
        ['Red', 'Green', 'White'],
        ['Red', 'Black'],
        ['Yellow']])

list_of_series = list_of_series.apply(pd.Series).stack().reset_index(drop=True)

#Sort a Series

s = pd.Series(['100','200','python','300.12','400'])
sorted_series = s.sort_values()

#s = pd.Series(['100',200,'python',300.12,'400'])
#sorted_series = s.sort_values()


#adding to a Series
s = s. append(pd.Series(['500','php'])).reset_index(drop=True)

#Write a Pandas program to calculate the frequency counts of each unique
# value of a given series.

import random
list1 = [random.randrange(1,10) for i in range(0,100)]
s = pd.Series(list1)
result = s.value_counts()

print()
