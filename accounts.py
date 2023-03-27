#Week03
#Author: Sarah Hastings
#This program reads in a 10 character account number 
#Outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).

accountno = input("Please enter an 10 digit account number:")

#below will take only input of 10 numbers, keep asking until enters 10 numbers
#while len(accountno) != 10:    #accountno = input('That was not a 10 digit number. Please enter your 10 digit number \n')
#    Bank = accountno[-4:].rjust(len(accountno), 'X')
#    print(Bank)
   
Bank = accountno[-4:].rjust(len(accountno), 'X')
print(Bank)

#Extra:
#This will take input of Modify the program to deal with account numbers of any length 
