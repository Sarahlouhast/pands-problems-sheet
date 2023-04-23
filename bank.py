#Week 2 
#Author: Sarah Hastings
#The program should prompt the user and read in two money amounts (in cent), 
#Add the two amounts
#Print out the answer in format with a euro sign and decimal point between the euro and cent of the amount 
#Reference: https://www.w3schools.com/python/python_numbers.asp 
           #https://www.w3schools.com/python/python_howto_add_two_numbers.asp 
           #https://stackabuse.com/format-number-as-currency-string-in-python/ 


#Prompt the user to enter integar amounts 
num1 = int(input("Enter amount1(in cent):"))
num2 =  int(input("Enter amount2(in cent):"))
sum= num1 + num2                                    #Calculate the sum of the values entered
format_sum = format(sum/100)                        #Format the value

print (f"The sum of these is €{format_sum}")        



