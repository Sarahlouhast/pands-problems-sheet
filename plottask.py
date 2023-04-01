#Week 8 
#Author: Sarah Hastings
#This displays: a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
#and a plot of the function  h(x)=x3 in the range [0, 10], on the one set of axes.

# Reference:  https://www.geeksforgeeks.org/how-to-plot-normal-distribution-over-histogram-in-python/
            # https://matplotlib.org/1.5.3/users/style_sheets.html

import numpy as np
import matplotlib.pyplot as plt


x = np.random.normal(5, 2, 1000)

#plt.hist(x)
plt.style.use('ggplot')
plt.hist(x, color='lightgreen', ec='black')
plt.xlabel("X axis", fontsize=16)  
plt.ylabel("Y axis", fontsize=16)
plt.xticks(fontsize=14)  
plt.yticks(fontsize=14)
plt.show() 


