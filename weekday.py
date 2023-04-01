#Week 5
#Author: Sarah Hastings
#This program outputs whether or not today is a weekday. 
#On a weekday it will output "Yes, unfortunately today is a weekday."
#On the weekend it will output "It is the weekend, yay!"
#Reference https://www.w3schools.com/python/python_datetime.asp , https://www.programiz.com/python-programming/datetime/current-datetime, 
#https://www.datacamp.com/tutorial/python-datetime

#from datetime import date #first need to import "datetime" to work with dates as date objects.

#Below is shorter option, tidier code 
from datetime import datetime
# Get Day Number from weekday
weekno = datetime.today().weekday()
 
if weekno < 5:
    print("Yes, unfortunately today is a weekday.")
else:  
    # 5 Sat, 6 Sun
    print("It is the weekend, yay!")