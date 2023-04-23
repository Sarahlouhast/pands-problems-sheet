#Weekly task 07
#Author: Sarah Hastings
#This program reads in a text file. It will take the filename from an argument on the command line.
#The program will then output the number of e's the text file contains. 
#Reference  https://www.pythonforbeginners.com/system/python-sys-argv ,
            #https://stackoverflow.com/questions/18047879/opening-files-with-python , 
            #https://www.w3schools.com/python/python_try_except.asp , 
            #https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/ ,
            #https://www.w3schools.com/python/python_try_except.asp

import sys
filename= sys.argv[1] #sys.argv is a list that contains all the arguments passed to the script on the command line

def letterFrequency(fileName, letter):          #This function is created to return the letter count in the text file
    try:                                        #Adding the try except incase the filename entered does not exist
        file = open(fileName, 'r')              #This will open the file in read mode
        text = file.read()                      #This will store the content of the file in a variable
        return text.count(letter)               #Using the count() function to return the number of times a given value/letter occurs in the file
    except FileNotFoundError:
        print("Filename (", filename,") does not exist. Please re-run and enter a valid filename.", sep = '')
        sys.exit(1)

print(letterFrequency((filename), 'e'), (f"occurences of 'e' in the text file.")) #This will call the function and display the letter count of occurences of lower case'e'
