
# **PANDS PROJECT**
### *This repository contains my project* 
### *for Programming and Scripting module* 
### *of Higher Diploma in Computing in Data Analytics course 2023* 
### *in Atlantic Technological University*
#
#

## Project objectives:
### 1. Research the Fisher's Iris data set online and write a summary about it. 
### 2. Using Python write a program called analysis.py. This program should perform analysis of Iris data set and output results in various formats. 
### 3. Discuss results of performed analysis
#
#

## List of analysis performed by program: 
###     1 Summary of each variable (*saved to a single text file*), 
###     2 Histogram of each variable (*saved to png file*), 
###     3 Scatter plot of each pair of variables, 
###     4 Heatmap correlation index of each pair of variables,
###     5 Box plot of each variable.
#
#
# About Iris data set.

<img src="https://user-images.githubusercontent.com/123666667/237202380-65147be2-dd8f-4cbe-ac05-2878816b856c.jpg" width="200" height="200"/>

## History 
##### [10]
The Iris flower dataset also known as Fisher's Iris dataset or Anderson's Iris dataset was collected by Edgard Anderson in 1935 and become famous after Ronald Fisher's publication in 1936 "The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis."

 Iris dataset is popular choice for beginners data analytics to practise various methods of analysis and visualisation of data.
#
## Structure 
##### [11]
Several variations of Iris dataset can be found, due to publishing errors.
The one used in this project was taken from UCI Machine Learning Repository [1] 

<img src="https://user-images.githubusercontent.com/123666667/237219678-2e0e07f2-509c-405e-b37b-c02e802bd1a2.png" width="200" height="200"/>

#

<img src="https://user-images.githubusercontent.com/123666667/237949679-a3321617-8115-4922-b912-bad7e02fa808.png" width="400" height="200"/>

The dataset has 150 records and five attributes: sepal length, sepal width, petal length, petal width and species. All measurements recorded in centimetres

<img src="https://user-images.githubusercontent.com/123666667/237952015-0c6e7a12-d030-423f-83c2-50c0ed28b49e.png" width="400" height="150"/>


Each of three represented species (Setosa, Virginica and Versicolor) has same number of records - 50 what makes this dataset balanced. 

## Analysis
##### [2, 7, 8, 9]
In this project we use Python to analyse Iris dataset. A few libraries were used for this analysis and data visualization: pandas, numpy, matplotlib.pyplot, seaborn.

 
###     1 Summary of each variable (*saved to a single text file*)
##### [3, 4] 
<img src="https://user-images.githubusercontent.com/123666667/237938937-585bb2bd-ce03-43c2-82eb-db45830f9f66.png" width="400" height="200"/>


Here we can see following values of each variable in dataset:

number of rows- how many entries variable has;

mean -average value of variable;

standard deviation -typical distance between each point and mean- the smaller number the more consistent dataset;

minimum - smallest value;

25%, 50% (median), 75% - values on positions corresponding to lower quarter, middle and upper quarter;

maximum - largest value.


###     2 Histogram of each variable (*saved to png file*) 
##### [5, 6]
Histogram visualise how often each value appears in a dataset

<img src="https://user-images.githubusercontent.com/123666667/237216112-3450d9b2-6084-4f75-bacb-abc92d5017c3.png" width="400" height="400"/>

We can see that there is an overlap between species in sepal measurements. Petal measurements a specially petal length can be used to identify Iris Setosa.

 
###     3 Scatter plot of each pair of variables

Scatter plot visualise relationship between two variables.

<img src="https://user-images.githubusercontent.com/123666667/237209230-f863ab0a-ee60-4a3b-818f-ea6cec3bad92.png" width="400" height="400"/>

Here again we can confirm that petal measurements are suitable for separating Iris Setosa from other two species. Also it is possible to classify Iris Virginica and Iris Versicolor based on petal size but with some lever of overlapping. 
#
###     4 Heatmap correlation coefficient of each pair of variables

Heatmap is way of visualising a correlation coefficient between two variables.
It is value between 1 and -1

1 is perfect positive correlation (as one variable increases the other one will increase too)

-1 is perfect negative correlation (as one variable increases the other decreases).

<img src="https://user-images.githubusercontent.com/123666667/237212641-36a1db88-c6ac-4adb-afa3-cf457dd0c5a0.png" width="400" height="400"/>



Here is an example how you can jump to a wrong conclusion if you don't know the structure of your dataset.
Looking at the heatmap of full Iris data set we can see negative correlation between some pairs of variables. We can say that for example if petal length is increasing sepal width should decrees as correlation index is -0.42.
but if you look at the heatmap of each species separately there is no negative correlation at all. Each measurement will increase if one of the others is increasing. Not all of them at the same rate.

It is easier to understand how three positive values from each subset become a negative in a whole set if you look at the scatter plot of pairs of variables where you can notice different dynamics in subsets and a set.


###     5 Box Plot 
Box-and-whisker plot is visualising statistical summary of each variable. The box represents middle 50% of score- between 25% and 75%. the line in the box- median value. The whiskers-lower 25% and upper 25%. Outliers- data points set far from the central values.

<img src="https://user-images.githubusercontent.com/123666667/237213422-71967bb4-6f81-4d63-94cd-9062efc90904.png" width="400" height="400"/>

It is very clear from this plot that Iris Virginica is largest of three species except one measurement-sepal width. Iris Setosa on the other hand is the smallest of three but has the widest sepal.

## Conclusion
Analyses performed on Iris data set in this project allow as to say that in any given dataset results from its subsets can be significantly different from results of full set. Therefore, it is important to check all possible combination before making any prognosis or recommendations based on data. 

For the porpoise of classification of Iris flowers most useful proved to be petal measurements. We can confidently separate Iris Setosa. Using petal width, it is possible with some degree of accuracy to identify Iris Virginica and Iris Versicolor with just the biggest samples of Versicolor and smallest of Virginica overlapping.


# References

#### [1] [UC Irvine Machine Learning Repository. Iris data set.](http://archive.ics.uci.edu/ml/datasets/Iris)

#### [2] [Exploratory Data Analysis of IRIS Data Set Using Python](https://medium.com/@avulurivenkatasaireddy/exploratory-data-analysis-of-iris-data-set-using-python-823e54110d2d)

#### [3] [How to Generate a Data Summary in Python](https://learnpython.com/blog/how-to-summarize-data-in-python/)

#### [4] [Directing print output to a .txt file](https://stackoverflow.com/questions/36571560/directing-print-output-to-a-txt-file)

#### [5] [How to plot in multiple subplots](https://stackoverflow.com/questions/31726643/how-to-plot-in-multiple-subplots)

#### [6] [Matplotlib Subplot Spacing: 4 Different Approaches](https://www.pythonpool.com/matplotlib-subplot-spacing)

#### [7] [Iris Data Analysis and Machine Learning(Python)](https://www.kaggle.com/code/adityabhat24/iris-data-analysis-and-machine-learning-python)

#### [8] [Classification Basics: Walk-through with the Iris Data Set](https://towardsdatascience.com/classification-basics-walk-through-with-the-iris-data-set-d46b0331bf82)

#### [9] [Exploratory data analysis (EDA) on Iris Dataset using Python](https://medium.com/@rishav.jnit/exploratory-data-analysis-eda-on-iris-dataset-using-python-cadd850c1fc6)

#### [10] [Iris flower data set](https://en.wikipedia.org/wiki/Iris_flower_data_set)

#### [11] [Will the real iris data please stand up?](https://ieeexplore.ieee.org/document/771092)