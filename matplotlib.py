#We can use matplotlib library to plot data.
#We first need to import matplotlib. It's standard  practice to nickname it plt.

import matplotlib pyplot as plt
import pandas as pd

readData = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')

#We use the scatter function to plot our data. The first argument of the sclatter function is the x-axis(horizontal direction) and the 
#second argument is the y-axis(vertical direction).

plt.scatter(readData['Age'], readData['Fare'])
plt.xlabel('Age')
plt.ylabel('Fare')

#We can also use our data to color code our scatter plot.
plt.scatter(readData['Age'],readData['Fare'], c=readData['Pclass'])

#A scatter plot is used to show all the values from your data on a graph. In order to get a visual representation of our data, we have to
#limit our data to two features.
#In matplotlib, we use the scatter function to create a scatter plot function for a line.


