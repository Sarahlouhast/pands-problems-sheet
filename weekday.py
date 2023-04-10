#Weekly task 05
#Author: Sarah Hastings
#This program outputs whether or not today is a weekday. 
#On a weekday it will output "Yes, unfortunately today is a weekday."
#On the weekend it will output "It is the weekend, yay!"
#Reference   https://www.w3schools.com/python/python_datetime.asp , 
            #https://www.programiz.com/python-programming/datetime/current-datetime , 
            #https://www.datacamp.com/tutorial/python-datetime
            
from datetime import datetime       #Firstly need to import "datetime" to work with dates

weekno = datetime.today().weekday() # Get Day Number from weekday
 
if weekno < 5:
    print("Yes, unfortunately today is a weekday.")
else:  
    print("It is the weekend, yay!") # 5 Sat, 6 Sun