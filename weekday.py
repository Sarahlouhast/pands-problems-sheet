#Weekly task 05
#Author: Sarah Hastings
#This program outputs whether or not today is a weekday. 
#On a weekday it will output "Yes, unfortunately today is a weekday."
#On the weekend it will output "It is the weekend, yay!"
#Reference   https://www.w3schools.com/python/python_datetime.asp , 
            #https://www.programiz.com/python-programming/datetime/current-datetime , 
            #https://www.datacamp.com/tutorial/python-datetime
            #https://pythontic.com/datetime/date/weekday 


from datetime import datetime        #Firstly need to import "datetime" to work with dates

weekno = datetime.today().weekday()  #Get Day Number from weekday, storing this in a variable called weekno
 
if weekno < 5:                       #Using the weekday method integer values for 0-4 relate to Monday-Friday, while 5,6 are Saturday,Sunday, <5 here will relate to any weekdays
    print("Yes, unfortunately today is a weekday.")
else:  
    print("It is the weekend, yay!") #If not <5, then here 5(Saturday), 6 (Sunday) will relate to weekend days