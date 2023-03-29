#Weekly task 7
#Author: Sarah Hastings
#This program reads in a text file
#Outputs the number of e's it contains. 
#The program should take the filename from an argument on the command line. (import sys)

import sys

filename= sys.argv[1]

def letterFrequency(fileName, letter):
    # open file in read mode
    file = open(fileName, 'r')
 
    #store content of the file in a variable
    text = file.read()
    #using count()
    return text.count(letter)
 
 
# call the function and display the letter count
print(letterFrequency('week7.txt', 'e'))
