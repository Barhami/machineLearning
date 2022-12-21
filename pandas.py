#Reading data with pandas
import pandas as pd
readData = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')
print(df)#head() to print only the head of the data
#Summarize the data
summarizeData = pd.summary('https://sololearn.com/uploads/files/titanic.csv')
print(df.describe())
#Count : This is the number of rows that have a value.
#Mean : Recall that the mean is the standars average.
#Std :This is short for standard deviation. This is a measure of how dispersed the data is.
#Min : The smallest value.
#25% : The 25% percentile or the first quartile.
#50% : The 50% percentile or the second quartile or the median.
#75% : The 75% percentile or the third quartile.
#Max : The largest value.

#Selecting a single column
column = readData['Fare']
print(column.head())
#selecting multiple column
columns = readData[['Age', 'Sex', 'Survived']]
print(columns.head())
#Creating a column
readData['male']= df['Sex'] == 'male'
print(readData.head())


