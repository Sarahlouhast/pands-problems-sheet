#bank.py
#Author: Sarah Hastings
#read in int, print out, add and return in euro.cent

num1 = int(input("Enter amount1(in cent):"))


num2 =  int(input("Enter amount2(in cent):"))
sum= num1 + num2
format_sum = format(sum/100)

print (f"The sum of these is €{format_sum}")



