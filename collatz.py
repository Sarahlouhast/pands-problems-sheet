#Week 4
#Author: Sarah Hastings
#This program asks the user to input any positive integer and outputs the successive values of the following calculation.
#At each step calculate the next value by taking the current value 
#And, if it is even, divide it by two, 
#But if it is odd, multiply it by three and add one.
#Have the program end if the current value is one.
#References:  https://www.w3schools.com/python/ref_func_print.asp 
            #https://data-flair.training/blogs/python-operator/  
            #https://github.com/HenkT28/pands-problem-set/blob/master/collatz.py 
            #https://www.w3schools.com/python/ref_func_print.asp 

#n allows user to enter a number
n = int(input("Please enter a positive integer: "))


while n !=1:                    #While loop will continue until n is 1   
    print(n, end= ' ')
    if n % 2 == 0:              # A number is even if division by 2 gives a remainder of 0   
        n = n // 2              # To avoid decimal, use floor division with, this will always give a integer value    
                                # https://data-flair.training/blogs/python-operator/    
    else:
        n = n * 3 + 1           #Else is needed for odd numbers, where remainder is 1, multiply *3 +1 
else:
        print(n, end= ' ')      #end= ' ' allows you choose what you want to be printed after the print statement has been executed
                                


