#week 4
#Author: Sarah Hastings
#This program asks the user to input any positive integer and outputs the successive values of the following calculation.
#At each step calculate the next value by taking the current value 
#and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
#Have the program end if the current value is one.

n = int(input("Please enter a positive integer: "))

while n !=1:
    print(n, end= ' ')
    if n % 2 == 0:
        n = n // 2   # To avoid decimal use floor division with // that always give a int    
                     # #https://data-flair.training/blogs/python-operator/    
    else:
        n = n * 3 + 1
else:
        print(n, end= ' ')


