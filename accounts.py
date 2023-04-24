#Weekly task 03
#Author: Sarah Hastings
#This program reads in a 10 character account number 
#Outputs the account number with only the last 4 digits showing and the first 6 digits replaced with Xs.
#Reference:  https://www.w3schools.com/python/python_strings_slicing.asp , 
            #https://www.freecodecamp.org/news/python-slicing-how-to-slice-an-array/ , 
            #https://www.w3schools.com/python/ref_string_rjust.asp


#The below will take only input of 10 numbers, keep asking until the user enters 10 numbers, print error message if 10 digits are not entered
while True:
    accountno = input("Please enter an 10 digit account number:")
    if len(accountno) !=10:
        print('That was not a 10 digit number. Please enter your 10 digit number \n')
    else:
        Bank = accountno[-4:].rjust(len(accountno), 'X')                #When 10 digits are entered, the rjust() method will right align the string using X as the fill character to anything before the last 4 digits
        print(Bank)
        break

#Extra step to the program:
#Remove the comments below to run this. This will modify the program to deal with account numbers of any length 
#And assuming the next step is to display only the last 4 characters, all other numbers will be replaced with Xs and the end result printed out.

#account_no_1 = input("Please enter an account number: ")
#print("x" * (len(account_no_1) - 4) + account_no_1[-4:])