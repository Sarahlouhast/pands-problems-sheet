# pands-problems-sheet

Author: Sarah Hastings
Course: 22-23: HDip in Computing in Data Analytics
Subject: Programming and Scripting

This file contains the files for the weekly tasks saved to location pands-problems-sheet

https://github.com/Sarahlouhast/pands-problems-sheet.git

Below is a list of each file name and what the program will do once executed. 


$ hello world.py 
File 1 - Week 1 task called hello world
This file should contain a python program that displays Hello World! when it is run.

$ bank.py 
File 2 - Week 2 task called bank.py 
This program should prompt the user and read in two money amounts (in cent)
Add the two amounts
Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount 
For example 
$ python bank.py
Enter amount1(in cent): 65
Enter amount2(in cent): 180
The sum of these is €2.45

$ accounts.py 
File 3 - Week 3 task called accounts.py 
This program that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs).
Modify the program to deal with account numbers of any length 
For example
$ python accounts.py
Please enter an 10 digit account number: 1234567890
XXXXXX7890
Extra:


$ collatz.py 
File 4 - Week 4 task, called collatz.py,
This program asks the user to input any positive integer and outputs the successive values of the following calculation.
At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one.
Have the program end if the current value is one.

For example
$ python collatz.py

Please enter a positive integer: 10

10 5 16 8 4 2 1

$ weekday.py
File 5 - Week 5 task, called weekday.py,
This program outputs whether or not today is a weekday. 
An example of running this program on a Thursday is given below.

$ python weekday.py
Yes, unfortunately today is a weekday.
An example of running it on a Saturday is as follows:
$ python weekday.py
It is the weekend, yay!

$ squareroot.py
File 6 - Week 6 task, called squareroot.py,
This program takes a positive floating-point number as input and outputs an approximation of its square root.
This program will use the newton method at estimating square roots.

For example
$ python squareroot.py
Please enter a positive number: 14.5
The square root of 14.5 is approx. 3.8.

$ moby-dick.py
File 7 - Week 7 task, called moby-dick.py,
This program reads in a text file and outputs the number of e's it contains. 
The program should take the filename from an argument on the command line. 

For example
$ python es.py moby-dick.txt
116960

$ plottask.py
File 8 - Week 8 task, called plottask.py,
This program displays a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, 
and a plot of the function  h(x)=x3 in the range [0, 10], 
on the one set of axes.
