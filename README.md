
# **PANDS PROJECT**
### *This repository contains my project* 
### *for Programming and Scriptind module* 
### *of Higher Diploma in Computing in Data Analytics course 2023* 
### *in Atlantic Technological University*
#
#

## Project objectives:
### 1. Research the Fisher's Iris data set online and write a summary about it. 
### 2. Usinf Python write a program called analysis.py. This programm should perfom analysis of Iris data set and output results in varios formats. 
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
The Iris flower data set also known as Fisher's Iris data set or Anderson's Iris data set was collected by Edgard Anderson in 1935 and become famous after Ronald Fisher's publication in 1936 "The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis."

 Iris data set is popular choise for beginers data analytics to practise varios methods.
#
## Structure 
##### [11]
Several varations of Iris dataset can be found, due to published errors.
The one used in this project was taken from UCI Machine Learning Repository [1] 

The dataset has 150 records and five attributes: sepal length, sepal width, petal length, petal width and species. All measurments recorded in centimeters

<img src="https://user-images.githubusercontent.com/123666667/237219678-2e0e07f2-509c-405e-b37b-c02e802bd1a2.png" width="200" height="200"/>

Each of three represented species (Setosa, Virginica and Versicolor) has equal number of records - 50 this makes this dataset balanced. 

## Analysis
##### [2, 7, 8, 9]
In this project we use Python to analyse Iris data set. A few libraryes were used for this analysis and data visualization: pandas, numpy, matplotlib.pyplot, seaborn.

 
###     1 Summary of each variable (*saved to a single text file*)
##### [3, 4] 
<img src="https://user-images.githubusercontent.com/123666667/237216963-23b3fad0-7d37-4b73-ad00-a5087579d80b.png" width="400" height="100"/>


Here we can see maximum, minimum, mean (average) and median (middle) value of each variable of dataset.


###     2 Histogram of each variable (*saved to png file*) 
##### [5, 6]
Histogram visualise how often each value appearse in a dataset

<img src="https://user-images.githubusercontent.com/123666667/237216112-3450d9b2-6084-4f75-bacb-abc92d5017c3.png" width="400" height="400"/>

We can see that there is an overlap betwenn spesies in sepal mesurments. Petal mesurment a specialy petal length can be used to identify iris setosa.

 
###     3 Scatter plot of each pair of variables

Scatter plot visualise relationship between two variables.

<img src="https://user-images.githubusercontent.com/123666667/237209230-f863ab0a-ee60-4a3b-818f-ea6cec3bad92.png" width="400" height="400"/>

Here again we can confirm that petal mesurments are seutible for separating iris senosa from other two spesies. Also it is possible to classify iris virginica and iris versicolor basd in petal size but with some lever of overlaping. 
#
###     4 Heatmap correlation coefficient of each pair of variables

Heatmap is way of visualising a correlation coefficient between two variables.
It is value betwen 1 and -1

1 is perfect positive correlation (as one variable increases the other one will increase too)

-1 is perfect negative correlation (as one variable increases the other decreases).

<img src="https://user-images.githubusercontent.com/123666667/237212641-36a1db88-c6ac-4adb-afa3-cf457dd0c5a0.png" width="400" height="400"/>



Here is an example how you can jump to a wrong conclusion if you don't know the structure of your dataset.
Looking at the heatmap of full Iris data set we can see negative correlation between some pairs of variables. so we can say that for example if petal length is increasing sepal width sould decrees as correlation index is -0.42.
but if you look at the heatmap of each species separatly there is no negative correlation at all. so each mesurment will increas if one of the is increasing. Not all of them at the same rate.

It is easier to understand how three positive values from each subset become a negative in a whole set if you look at the scatter plot of pairs of variables where you can notice different dinamycs in subsets and a set.


###     5 Box Plot 
Box-and-whisker plot is visualising statistical summary of each variable. The box represents middle 50% of score- beween 25% and 75%. the line in the box- median value. The whiskers-lower 25% and upper 25%. Outliers- data points set far from the central values.

<img src="https://user-images.githubusercontent.com/123666667/237213422-71967bb4-6f81-4d63-94cd-9062efc90904.png" width="400" height="400"/>

It is very cleare from this plot that Iris virginica is largest of three species exept one mesurment-sepal width.

## Conclusion

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