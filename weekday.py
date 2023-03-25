#Week 5
#Author: Sarah Hastings
#This program outputs whether or not today is a weekday. 
#On a weekday it will output "Yes, unfortunately today is a weekday."
#On the weekend it will output "It is the weekend, yay!"
#Reference https://www.w3schools.com/python/python_datetime.asp , https://www.programiz.com/python-programming/datetime/current-datetime, 
#https://www.datacamp.com/tutorial/python-datetime

#from datetime import date #first need to import "datetime" to work with dates as date objects.
# Extract today date
#today = date.today()

#if today.weekday() == 0:
#    print("Yes, unfortunately today is a weekday.")
#elif today.weekday() == 1:
#    print("Yes, unfortunately today is a weekday.")
#elif today.weekday() == 2:
#    print("Yes, unfortunately today is a weekday.")
#elif today.weekday() == 3:
#    print("Yes, unfortunately today is a weekday.")
#elif today.weekday() == 4:
#    print("Yes, unfortunately today is a weekday.")
#elif today.weekday() == 5:
#    print("It is the weekend, yay!")
#else:
#    print("It is the weekend, yay!")


#Below is shorter option, tidier code 
from datetime import datetime
# Get Day Number from weekday
weekno = datetime.today().weekday()
 
if weekno < 5:
    print("Yes, unfortunately today is a weekday.")
else:  
    # 5 Sat, 6 Sun
    print("It is the weekend, yay!")