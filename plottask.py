#Week 8 
#Author: Sarah Hastings
#This displays: a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
#and a plot of the function  h(x)=x3 in the range [0, 10], on the one set of axes.

# Reference:  https://www.geeksforgeeks.org/how-to-plot-normal-distribution-over-histogram-in-python/
            # https://matplotlib.org/1.5.3/users/style_sheets.html
            # https://scriptverse.academy/tutorials/python-matplotlib-plot-function.html 
            # https://numpy.org/doc/stable/reference/generated/numpy.linspace.html
            # https://data-flair.training/blogs/numpy-applications/ 

import numpy as np                      #Firstly import numpy, this will allow you to work with arrays, numerical data, mathematical operations
import matplotlib.pyplot as plt         #Import matplotlib.pyplot, this will allow you to create plots, histograms, decorate these with labels amd much more 

x = np.random.normal(5, 2, 1000)        #Variable x is set here and contains the random.normal method which has 3 parameters (mean, standard deviation, the total number of samples to be drawn), in this case 1000 values with a mean of 5 and standard deviation of 2

plt.style.use('ggplot')                 #This will add a style to the plot, in this case grey background with white grid lines
plt.hist(x, color='lightgreen', ec='black', label='Normal Distribution')      #This will plot the histogram, give colour lightgreen to the bar and the edges colour black and also label the histogram 
plt.xlabel("X-Axis", fontsize=16)       #Create label,fontsize for the axis
plt.ylabel("Y-Axis", fontsize=16)
plt.xticks(fontsize=14)                 #Create fontsize for the axis values
plt.yticks(fontsize=14)


x_range = np.linspace(0, 10, 100)       #x_range variable is set and contains the linspace method which will add the plot of the function h(x) = x^3 which will be created next, in the range [0, 10], with 100 numbers
y = x_range ** 3                        #The cubed function is defined here. If you want to amend this cubed function to squared function for example this can be done easily by changing - y = x_range ** 2 ( and amend the label name in the code to h(x) = x^2)
plt.plot(x_range, y, color='blue', label='Function h(x) = x^3') #Plot the cubed function, color & label


plt.legend(fontsize=14)                 #This function will display the legend - the labels for histogram function as "Normal Distribution" and the cubed function as "Function h(x) = x^3"

#plt.savefig('My_plot.png') If you want to save your plot use can do so here, note ensure this function is called before the show function, otherwise if it is after the show function your image will be blank

plt.show()                              #Display the plot, note you will need to close out of this if you want to end and run another task

