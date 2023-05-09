# analysis.py
# Author: Olga Knutva
# Description: 1. Outputs a summary of each variable to a single text file, 
#               2. Saves a histogram of each variable to png files, and 
#               3. Outputs a scatter plot of each pair of variables. 
#               4. Other analysis:
#                    4.1 heatmap
#                    4.2 box

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
iris_all=pd.read_csv('iris.data', names=col)

iris_setosa=iris_all.loc[iris_all["class"]=="Iris-setosa"]
iris_virginica=iris_all.loc[iris_all["class"]=="Iris-virginica"]
iris_versicolor=iris_all.loc[iris_all["class"]=="Iris-versicolor"]

# 1.Outputs a summary of each variable (min, max, median, mean ) to a single text file
#https://learnpython.com/blog/how-to-summarize-data-in-python/
#https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file

def save_txt_summary():
    with open("Summary of variables.txt", "a") as f:
        print (iris_all[[col_sl, col_sw, col_pl, col_pw]].apply(["max", "min", "mean", "median"]), file=f)

#2. Saves a histogram of each variable to png files
def histogram(pos, title, colname):
    plt.subplot(2, 2, pos)
    plt.title(title)
    plt.xlabel(f'{title.lower()} in cm')
    plt.ylabel("number of samples")
    plt.hist(iris_all[colname],            color='paleturquoise',  edgecolor='blue')
    plt.hist(iris_setosa[colname],     color='lightcoral',     edgecolor='red')
    plt.hist(iris_virginica[colname],  color='cornflowerblue', edgecolor='red')
    plt.hist(iris_versicolor[colname], color='plum',           edgecolor='red')

def save_png_histogram():
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
    plt.clf()


#3. Outputs a scatter plot of each pair of variables

def scatter(pos, colname_x, colname_y):
    plt.subplot(2, 2, pos)
    plt.title(f'{colname_x} V {colname_y}')
    plt.xlabel(f'{colname_x.lower()} in cm')
    plt.ylabel(f'{colname_y.lower()} in cm')
    plt.scatter(iris_setosa[colname_x],     iris_setosa[colname_y],     color='lightcoral',     edgecolor='red')
    plt.scatter(iris_virginica[colname_x],  iris_virginica[colname_y],  color='cornflowerblue', edgecolor='blue')
    plt.scatter(iris_versicolor[colname_x], iris_versicolor[colname_y], color='plum',           edgecolor='purple')
    plt.grid()

def show_scatter():
    scatter(1, "sepal_length", "sepal_width")
    scatter(2, "petal_length", "petal_width")
    scatter(3, "petal_width", "sepal_width")
    scatter(4, "petal_length", "sepal_length")

    plt.subplots_adjust(left=0.1, 
                        bottom=0.1,  
                        right=0.9,  
                        top=0.9,  
                        wspace=0.4,  
                        hspace=1.3)
    plt.figlegend(["iris setosa", "iris virginica", "iris versicolor"], loc="center")
    plt.suptitle('IRIS SCATTER PLOT OF EACH PAIR OF VARIABLES')

    plt.show()

"""
# other way of getting scatter plot of each pair of variables. 
#it is represenitg all possible combination of pairs 
#but looks too overcrouded to me with duplication of same pairs where variables just positioned on different axes.
from pandas.plotting import scatter_matrix
# scatter plot matrix
scatter_matrix(iris_all,figsize=(10,10))

plt.show()
#https://www.kaggle.com/code/adityabhat24/iris-data-analysis-and-machine-learning-python

"""

# 4. Other analysis 

#       4.1 Heat map https://towardsdatascience.com/classification-basics-walk-through-with-the-iris-data-set-d46b0331bf82
def heatmap(pos, data_set, title):
    plt.subplot(2, 2, pos )
    plt.title(title)
    sns.heatmap(data_set.corr(), linecolor = 'white', linewidths = 1, annot = True )

def show_heatmap():
    heatmap(1, iris_all, "IRIS ALL SPECIES")
    heatmap(2, iris_setosa, "IRIS SETOSA")
    heatmap(3, iris_versicolor, "IRIS VERSICOLOR")
    heatmap(4, iris_virginica, "IRIS VIRGINICA")

    plt.subplots_adjust(left=0.1, 
                        bottom=0.1,  
                        right=0.9,  
                        top=0.9,  
                        wspace=0.4,  
                        hspace=0.5)

    plt.show()

#       4.2 Box-plot https://medium.com/@rishav.jnit/exploratory-data-analysis-eda-on-iris-dataset-using-python-cadd850c1fc6

def box(pos, colname_y):
    plt.subplot(2, 2, pos)
    plt.title(colname_y.upper())
    sns.boxplot(x="class",y=colname_y, data=iris_all)

def show_box():
    box(1, "petal_length")
    box(2, "petal_width")
    box(3, "sepal_length")
    box(4, "sepal_width")

    plt.subplots_adjust(left=0.1, 
                        bottom=0.1,  
                        right=0.9,  
                        top=0.9,  
                        wspace=0.4,  
                        hspace=0.5)

    plt.suptitle('IRIS BOX PLOT OF EACH VARIABLE')
    plt.show()

# List of function for each plot for easy navigation

save_txt_summary()
save_png_histogram()
show_scatter()
show_heatmap()
show_box()
