#Week 2 
#Author: Sarah Hastings
#The program should prompt the user and read in two money amounts (in cent), 
#Add the two amounts
#Print out the answer in format with a euro sign and decimal point between the euro and cent of the amount 
#Reference: https://www.w3schools.com/python/python_numbers.asp 
           #https://www.w3schools.com/python/python_howto_add_two_numbers.asp 
           #https://stackabuse.com/format-number-as-currency-string-in-python/ 



num1 = int(input("Enter amount1(in cent):"))        #Prompt the user to enter integer amounts, which will be stored in num1, num2 
num2 =  int(input("Enter amount2(in cent):"))
sum= num1 + num2                                    #Calculate the sum of the values entered
format_sum = format(sum/100)                        #Format the value, stored in a variable to be used below

print (f"The sum of these is €{format_sum}")        #The sum result is printed out in the specified format



