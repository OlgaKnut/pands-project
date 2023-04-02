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

col_sl="sepal_length"
col_sw="sepal_width"
col_pl="petal_length"
col_pw="petal_width"

col=[col_sl, col_sw, col_pl, col_pw, 'class']
data=pd.read_csv('iris.data', names=col)

iris_setosa=data.loc[data["class"]=="Iris-setosa"]
iris_virginica=data.loc[data["class"]=="Iris-virginica"]
iris_versicolor=data.loc[data["class"]=="Iris-versicolor"]

#2. Saves a histogram of each variable to png files
def histogram(pos, title, colname):
    plt.subplot(2, 2, pos)
    plt.title(title)
    plt.xlabel(f'{title.lower()} in cm')
    plt.ylabel("number of samples")
    plt.hist(data[colname],            color='paleturquoise',  edgecolor='blue')
    plt.hist(iris_setosa[colname],     color='lightcoral',     edgecolor='red')
    plt.hist(iris_virginica[colname],  color='cornflowerblue', edgecolor='red')
    plt.hist(iris_versicolor[colname], color='plum',           edgecolor='red')

fig=plt.figure()
#https://stackoverflow.com/questions/31726643/how-to-plot-in-multiple-subplots
histogram(1, "SEPAL LENGTH", col_sl)
histogram(2, "SEPAL WIDTH",  col_sw)
histogram(3, "PETAL LENGTH", col_pl)
histogram(4, "PETAL WIDTH",  col_pw)

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



#3. Outputs a scatter plot of each pair of variables

fig2=plt.figure()
plt.subplot(2,2,1)
plt.scatter(iris_setosa[col_sl],iris_setosa[col_sw],color='lightcoral')
plt.scatter(iris_virginica[col_sl],iris_virginica[col_sw],color='cornflowerblue')
plt.scatter(iris_versicolor[col_sl],iris_versicolor[col_sw],color='plum')
plt.title("SEPAL LENGTH V SEPAL WIDTH")
plt.xlabel("sepal length in cm")
plt.ylabel("sepal width in cm")
plt.grid()

plt.subplot(2,2,2)
plt.scatter(iris_setosa[col_pl],iris_setosa[col_pw],color='lightcoral')
plt.scatter(iris_virginica[col_pl],iris_virginica[col_pw],color='cornflowerblue')
plt.scatter(iris_versicolor[col_pl],iris_versicolor[col_pw],color='plum')
plt.title("PETAL LENGTH V PETAL WIDTH")
plt.xlabel("petal length in cm")
plt.ylabel("petal width in cm")
plt.grid()

plt.subplot(2,2,3)
plt.scatter(iris_setosa[col_pw],iris_setosa[col_sw],color='lightcoral')
plt.scatter(iris_virginica[col_pw],iris_virginica[col_sw],color='cornflowerblue')
plt.scatter(iris_versicolor[col_pw],iris_versicolor[col_sw],color='plum')
plt.title("PETAL WIDTH V SEPAL WIDTH")
plt.xlabel("petal width in cm")
plt.ylabel("sepal width in cm")
plt.grid()

plt.subplot(2,2,4)
plt.scatter(iris_setosa[col_pl],iris_setosa[col_sl],color='lightcoral')
plt.scatter(iris_virginica[col_pl],iris_virginica[col_sl],color='cornflowerblue')
plt.scatter(iris_versicolor[col_pl],iris_versicolor[col_sl],color='plum')
plt.title("PETAL LENGTH V SEPAL LENGTH")
plt.xlabel("petal length in cm")
plt.ylabel("sepal length in cm")
plt.grid()

plt.subplots_adjust(left=0.1, 
                    bottom=0.1,  
                    right=0.9,  
                    top=0.9,  
                    wspace=0.4,  
                    hspace=1.3)
plt.figlegend(["iris setosa", "iris virginica", "iris versicolor"], loc="center")
plt.suptitle('IRIS SCATTER PLOT OF EACH PAIR OF VARIABLES')

plt.close(fig)

plt.show()