#Numpy is a python package for manipulating lists and tables of numerical data. We can use it to do a lot of statical calculations.
#a data object in numpy is called an Array

#Converting from a Pandas Series to a Numpy Array
#We just put the keyword values after the pandas intructions like this :
import pandas as pd
readData = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
print(df[['Pclass', 'Fare', 'Age']].values)
#Numpy shapes attribute
#We use the numpy shape attribute to determine the size of our numpy array.
arr = df[['Pclass', 'Fare', 'Age']].values
print(arr.shape)
#Select from a Numpy Array
arr[0, 1]
#Select a single row
arr[0]
#Select a single column 
arr[:,2]
#Masking
#Often times you want to select all the row that 
mask = arr[:,2]<18
#A mask is a boolean array(True/False values) that tell us which values from the array we're interested in.

#Summing and Counting
print(mask.sum())

