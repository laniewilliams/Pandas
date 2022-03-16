import pandas as pd

grades_dict = {'Wally':[87,96,70],
                'Eva':[100,87,90],
                'Sam':[94,77,90],
                'Katie':[100,81,82],
                'Bob':[83,65,85]}

grades = pd.DataFrame(grades_dict)
grades.index = ["Test1","Test2","Test3"]

print(grades)

eva = grades['Eva'] #can only do this with STRING INDEXES

sam = grades.Sam

#using the loc and iloc methods

test2 = grades.loc["Test2"] #loc is short for location

test1 = grades.iloc[1]

#for consecutive rows, ou just need a colon (:)

test1_thru_test3 = grades.loc['Test1':'Test3']

#For non-consecutive rows
test1_and_test3 = grades.loc[['Test1','Test3']]


test1_and_test2 = grades.iloc[0:2] #doesn't give you the upper index so to do the first 2 tests you have to do 0:2

#view only eva's and katie's grades for Test 1 and test2

test1_and_test2_EK = grades.loc[:'Test2',['Eva','Katie']] #Eva and Katie have to be in a list

#view only Sam's THRU Bob's grades for Test1 and Test3

sam_thru_bob_test1_test3 = grades.loc[['Test1','Test3'],'Sam':]

#Boolean Indexing
# Select everyone with an A grade

grades_A = grades[grades>=90]

# Create a dataframe for everyone with a B grade
grades_B = grades[(grades>=80) & (grades < 90)]

grades_A_or_B = grades[(grades>=90) | (grades >= 80)]

pd.set_option('precision',2)

# by student
print(grades.describe())

#by test
print(grades.T.describe())

#Exercise - Get the average of all the student grades on each test
print(grades.T.mean()) #calling a specific method


#Sort rows by their indices (Test name)

r_sorted_grades_i = grades.sort_index(ascending=False)

#sort columns by their column names (student names)
# axis = 1 indicates to sort by column indices
# axis = 0 indicates to sort by row indices

c_sorted_grades_i = grades.sort_index(axis=1)

#in reverse order
c_sorted_grades_i = grades.sort_index(axis=1,ascending=False)



print()