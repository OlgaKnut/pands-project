# analysis.py
# Author: Olga Knutva
# Description: 1. Outputs a summary of each variable to a single text file, 
#               2. Saves a histogram of each variable to png files, and 
#               3. Outputs a scatter plot of each pair of variables. 
#               4. Performs any other analysis you think is appropriate

#Ref https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
col=['sepal_length', 'sepal_width', 'petal_length', 'petal_width', 'class']
data=pd.read_csv('iris.data', names=col)

iris_setosa=data.loc[data["class"]=="Iris-setosa"]
iris_virginica=data.loc[data["class"]=="Iris-virginica"]
iris_versicolor=data.loc[data["class"]=="Iris-versicolor"]

fig =plt.figure()
#https://stackoverflow.com/questions/31726643/how-to-plot-in-multiple-subplots

plt.subplot(2,2,1)
plt.title("SEPAL LENGTH")
plt.xlabel("sepal length in cm")
plt.ylabel("number of samples")
plt.hist(data["sepal_length"], color='paleturquoise', edgecolor='blue')
plt.hist(iris_setosa["sepal_length"], color='lightcoral', edgecolor='red')
plt.hist(iris_virginica["sepal_length"], color='cornflowerblue', edgecolor='red')
plt.hist(iris_versicolor["sepal_length"], color='plum', edgecolor='red',)
         
plt.subplot(2,2,2)
plt.title("SEPAL WIDTH")
plt.xlabel("sepal width in cm")
plt.ylabel("number of samples")
plt.hist(data["sepal_width"], color='paleturquoise', edgecolor='blue')
plt.hist(iris_setosa["sepal_width"], color='lightcoral', edgecolor='red')
plt.hist(iris_virginica["sepal_width"], color='cornflowerblue', edgecolor='red')
plt.hist(iris_versicolor["sepal_width"], color='plum', edgecolor='red',)

plt.subplot(2,2,3)
plt.title("PETAL LENGTH")
plt.xlabel("petal length in cm")
plt.ylabel("number of samples")
plt.hist(data["petal_length"], color='paleturquoise', edgecolor='blue')
plt.hist(iris_setosa["petal_length"], color='lightcoral', edgecolor='red')
plt.hist(iris_virginica["petal_length"], color='cornflowerblue', edgecolor='red')
plt.hist(iris_versicolor["petal_length"], color='plum', edgecolor='red',)

plt.subplot(2,2,4)
plt.title("PETAL WIDTH")
plt.xlabel("petal width in cm")
plt.ylabel("number of samples")
plt.hist(data["petal_width"], color='paleturquoise', edgecolor='blue')
plt.hist(iris_setosa["petal_width"], color='lightcoral', edgecolor='red')
plt.hist(iris_virginica["petal_width"], color='cornflowerblue', edgecolor='red')
plt.hist(iris_versicolor["petal_width"], color='plum', edgecolor='red',)

#https://www.pythonpool.com/matplotlib-subplot-spacing
plt.subplots_adjust(left=0.1, 
                    bottom=0.1,  
                    right=0.9,  
                    top=0.9,  
                    wspace=0.4,  
                    hspace=1.3)
plt.figlegend(["all samples", "iris setosa", "iris virginica", "iris versicolor"], loc="center")
plt.suptitle('IRIS VARIABLES HISTOGRAMS')
plt.savefig('Iris_var_hist.png')
#plt.show()

#data.head()
#print(data.head())

#iris.plot(kind ="scatter",
#          x ='SepalLengthCm',
#         y ='PetalLengthCm')
#plt.grid()