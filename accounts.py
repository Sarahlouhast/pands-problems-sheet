#Week03
#Author: Sarah Hastings
#This program reads in a 10 character account number 
#Outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).
#Reference: https://www.w3schools.com/python/python_strings_slicing.asp ,https://www.freecodecamp.org/news/python-slicing-how-to-slice-an-array/ , https://www.w3schools.com/python/ref_string_rjust.asp

#User is prompted to enter a 10 digit number, there is no restriction on max amount of numbers that can be entered here
accountno = input("Please enter an 10 digit account number:")

#below will take only input of 10 numbers, keep asking until user enters 10 numbers
#while len(accountno) != 10:    
#    accountno = input('That was not a 10 digit number. Please enter your 10 digit number \n')

   
Bank = accountno[-4:].rjust(len(accountno), 'X')
print(Bank)