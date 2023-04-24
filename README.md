# Course: 22-23: HDip in Computing in Data Analytics
## Author: Sarah Hastings
### Subject: Programming and Scripting

This file contains the files for the weekly tasks for this course, saved to location [pands-problems-sheet](https://github.com/Sarahlouhast/pands-problems-sheet.git).
Below is a list of each file name, the code for the program, what the program will do once executed including a colde explanation, references used and also a link to the program location.
Also this file contains all links to references used to read this readme file.

## Weekly Task number 1

File 1 - Week 1 task called [hello world.py](https://github.com/Sarahlouhast/pands-problems-sheet/blob/main/helloworld.py). This file should contain a python program that displays Hello World! when it is run.

Code: 

```
print("Hello World!")
```

## Weekly Task number 2

File 2 - Week 2 task called [bank.py](https://github.com/Sarahlouhast/pands-problems-sheet/blob/main/bank.py). This program should prompt the user and read in two money amounts (in cent) Add the two amounts Print out the answer in a human readable format with a euro sign and decimal point between the euro and cent of the amount. 

For example 
Enter amount1(in cent): 65 
Enter amount2(in cent): 180 
The sum of these is €2.45

Code:

```
num1 = int(input("Enter amount1(in cent):"))
num2 =  int(input("Enter amount2(in cent):"))
sum= num1 + num2                                    
format_sum = format(sum/100)                       
print (f"The sum of these is €{format_sum}")
```

Code Explanation:

The user is prompted to enter integer amounts. 
These are stored in variables num1, num2. 
The sum is used to calculated the sum of the values entered.
The format_sum is used format the value.
And the result will be print with a string of text and the result formatted.

References:

* <https://stackabuse.com/format-number-as-currency-string-in-python/>
* <https://www.w3schools.com/python/python_numbers.asp>
* <https://www.w3schools.com/python/python_howto_add_two_numbers.asp>


## Weekly Task number 3 

File 3 - Week 3 task called [accounts.py](https://github.com/Sarahlouhast/pands-problems-sheet/blob/main/accounts.py). This program that reads in a 10 character account number and outputs the account number with only the last 4 digits showing (and the first 6 digits replaced with Xs). Modify the program to deal with account numbers of any length.

For example
Please enter an 10 digit account number: 1234567890 
XXXXXX7890 

Code:

```
while True:
    accountno = input("Please enter an 10 digit account number:")
    if len(accountno) !=10:
        print('That was not a 10 digit number. Please enter your 10 digit number \n')
    else:
        Bank = accountno[-4:].rjust(len(accountno), 'X')                
        print(Bank)
        break

account_no_1 = input("Please enter an account number: ")
print("x" * (len(account_no_1) - 4) + account_no_1[-4:])
```

Code Explanation:

Using a while loop this code will take only input of 10 numbers and keep asking until the user enters 10 numbers, printing an error message if 10 digits are not entered. Slicing is used to access the last 4 characters, this is a very useful method when accessing data/characters. The rjust function (right-justified) is used to fill the characters to the left and replace with "x", while keeping the data to the right the same, the right specified sliced length, in this case the last 4 characters. You will see in the comments the extra step to the program, remove the comments if you want to add this step, which will modify the program to deal with account numbers of any length, and assuming the next step is to display only the last 4 characters, all other numbers will be replaced with Xs and the end result printed out.


References:

* <https://www.w3schools.com/python/python_strings_slicing.asp>  
* <https://www.freecodecamp.org/news/python-slicing-how-to-slice-an-array/>  
* <https://www.w3schools.com/python/ref_string_rjust.asp> 

## Weekly Task number 4

File 4 - Week 4 task, called [collatz.py](https://github.com/Sarahlouhast/pands-problems-sheet/blob/main/collatz.py). This program asks the user to input any positive integer and outputs the successive values of the following calculation. At each step calculate the next value by taking the current value and, if it is even, divide it by two, but if it is odd, multiply it by three and add one. Have the program end if the current value is one.

For example 
Please enter a positive integer: 10
10 5 16 8 4 2 1

Code:

```
n = int(input("Please enter a positive integer: "))

while n !=1:                     
    print(n, end= ' ')
    if n % 2 == 0:                 
        n = n // 2                  
                                    
    else:
        n = n * 3 + 1            
else:
        print(n, end= ' ')                                    
```

Code Explanation:

The user is prompted to enter a positive integer, which is stored in variable n. 
A while loop is set up and will continue until n is 1 based on the program requirement to end at 1. 
An if statement (if n % 2 == 0:) is used to check is a number is even if division by 2 gives a remainder of 0.   
Using  n = n // 2, floor division to avoid decimals and this will always give an integer value.    
Else is needed for odd numbers, where remainder is 1, multiply *3 +1. 
And finally once n is 1, this will be printed and the program will end.                    

References:

* <https://data-flair.training/blogs/python-operator/> 
* <https://github.com/HenkT28/pands-problem-set/blob/master/collatz.py>  
* <https://www.w3schools.com/python/ref_func_print.asp> 

## Weekly Task number 5

File 5 - Week 5 task, called [weekday.py](https://github.com/Sarahlouhast/pands-problems-sheet/blob/main/weekday.py). 
This program outputs whether or not today is a weekday. An example of running this program on a Thursday is given below.

For example 
An example of running it on a weekday is as follows:Yes, unfortunately today is a weekday. 
An example of running it on a Saturday is as follows: It is the weekend, yay!

Code:

```
from datetime import datetime       
weekno = datetime.today().weekday() 
if weekno < 5:
    print("Yes, unfortunately today is a weekday.")
else:  
    print("It is the weekend, yay!") # 5 Sat, 6 Sun
```

Code Explanation:

Firstly, we must import module "datetime" to work with dates in Python. 
Using the datetime.today() to check the current local datetime, next the weekday() method returns the day of the week as an integer, where Monday is 0 and Sunday is 6, this will be storied in a variable called weekno.
Using the weekday method as integer values for 0-4 relate to Monday-Friday, while 5,6 are Saturday,Sunday, <5 will relate to any weekdays. If not <5, then 5(Saturday), 6 (Sunday) will relate to weekend days. The result will print out the given statement according to which day of the week it is.

References:

* <https://www.w3schools.com/python/python_datetime.asp>   
* <https://www.programiz.com/python-programming/datetime/current-datetime>  
* <https://www.datacamp.com/tutorial/python-datetime> 
* <https://pythontic.com/datetime/date/weekday> 

## Weekly Task number 6

File 6 - Week 6 task, called [squareroot.py](https://github.com/Sarahlouhast/pands-problems-sheet/blob/main/squareroot.py). This program takes a positive floating-point number as input and outputs an approximation of its square root. This program will use the newton method at estimating square roots.

For example 
Please enter a positive number: 14.5 
The square root of 14.5 is approx. 3.8.

Code:

```
num = float(input("Please enter a positive number: "))            

def newtonsqrt(n, tolerance=1e-10):                                                
    approx=0.5*n                                                                                      
    better=0.5*(approx+n/approx)                                  
    while abs(better - approx) > tolerance:                       
        approx=better                                             
        better=0.5*(approx+n/approx)                              
    return round(approx,1)
    
print(f"The square root of {num} is approx. {newtonsqrt(num)}.")  
```

Code Explanation:

Firstly the user is prompted to enter a positive floating point number.
The square root function is defined using the Newton-Raphson method, which has two parameters it will take in, a number and a tolerance, the tolerance is used to get accuracy.
Note the tolerance here is set to 1e-10 which is 1 multiplied by 10 to the power of -10, which is 0.0000000001, the function will continue to check the approx value until the difference between the current approx and the true square root is very small, up to a precision of 10 decimal places.                                                      
Variable approx is set to start with any approximation, half of the input number.
Then better, which will compute a better approximation using this formula (better=0.5*(approx+n/approx)).
A while loop is then added to check if the difference between better and approx is greater than the tolerance value, in this case comparing the absolute difference between better and approx to the tolerance value of 1e-10, the loop will stop when the difference is less than the tolerance level.          
Within this loop, approx is updated to the value of better and better is updated to the new approx value using a formula and the result to rounded to 1 decimal.
Finally the function is called and the output results printed.

References:

* <https://thirumalai2024.medium.com/python-program-to-find-square-root-of-the-number-using-newtons-method-937c0e732756> 
* <https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/>  
* <https://towardsdatascience.com/newton-raphson-explained-and-visualised-23f63da21bd5> 
* <https://runestone.academy/ns/books/published/thinkcspy/MoreAboutIteration/NewtonsMethod.html> 
* <https://www.simplilearn.com/tutorials/python-tutorial/float-in-python#:~:text=Float()%20is%20a%20method,as%20the%20floating%2Dpoint%20output.> 

## Weekly Task number 7

File 7 - Week 7 task, called [es.py](https://github.com/Sarahlouhast/pands-problems-sheet/blob/main/es.py), and sample file called [SampleFile.txt](https://github.com/Sarahlouhast/pands-problems-sheet/blob/main/SampleFile.txt) used to test the program. This program reads in a text file and outputs the number of e's it contains. The program should take the filename from an argument on the command line.

For example python es .py moby-dick.txt 
116960

Code:

```
import sys
filename= sys.argv[1] 

def letterFrequency(fileName, letter):          
    try:                                       
        file = open(fileName, 'r')              
        text = file.read()                      
        return text.count(letter)               
    except FileNotFoundError:
        print("Filename (", filename,") does not exist. Please re-run and enter a valid filename.", sep = '')
        sys.exit(1)

print(letterFrequency((filename), 'e'), (f"occurences of the letter 'e' in the text file.")) 
```

Code Explanation:

Firstly import sys which will provide access to some variables and functions used or maintained by the python interpreter, in this case we will need the sys.argv which is a list that contains all the arguments passed to the script on the command line. 
A function is created to return the letter count in the text file.
In this function a try except is used incase the filename entered does not exist. If it does not exist. An error message will be printed. 
Using file = open(fileName, 'r') will open the file in read mode.
Using text = file.read() will store the content of the file in a variable called text.
Using return text.count(letter) to return the number of times a given value/letter occurs in the file.
The function is called and printed using the below, displaying the letter count of occurences of lower case'e'.
print(letterFrequency((filename), 'e'), (f"occurences of 'e' in the text file."))

References:

* <https://www.pythonforbeginners.com/system/python-sys-argv> 
* <https://stackoverflow.com/questions/18047879/opening-files-with-python> 
* <https://www.w3schools.com/python/python_try_except.asp>  
* <https://www.geeksforgeeks.org/count-the-number-of-times-a-letter-appears-in-a-text-file-in-python/>

## Weekly Task number 8

File 8 - Week 8 task, called [plottask.py](https://github.com/Sarahlouhast/pands-problems-sheet/blob/main/plottask.py), This program displays a histogram of a normal distribution of a 1000 values with a mean of 5 and standard deviation of 2, and a plot of the function h(x)=x3 in the range [0, 10], on the one set of axes.

Code:

```
import numpy as np                    
import matplotlib.pyplot as plt        

x = np.random.normal(5, 2, 1000)        
plt.style.use('ggplot')             
plt.hist(x, color='lightgreen', ec='black', label='Normal Distribution')     
plt.xlabel("X-Axis", fontsize=16)       
plt.ylabel("Y-Axis", fontsize=16)
plt.xticks(fontsize=14)                 
plt.yticks(fontsize=14)

x_range = np.linspace(0, 10, 100)       
y = x_range ** 3                        
plt.plot(x_range, y, color='blue', label='Function h(x) = x^3') 

plt.legend(fontsize=14)  
#plt.savefig('My_plot.png')
plt.show()                              
```

Code Explanation:

Firstly import numpy, this will allow you to work with arrays, numerical data, mathematical operations.
Import matplotlib.pyplot, this will allow you to create plots, histograms, decorate these with labels amd much more.
Variable x is set and contains the random.normal method which has 3 parameters (mean, standard deviation, the total number of samples to be drawn), in this case 1000 values with a mean of 5 and standard deviation of 2.
plt.style.use('ggplot') will add a style to the plot, in this case grey background with white grid lines.
plt.hist will plot the histogram, give colour lightgreen to the bar and the edges colour black and also label the histogram. 
Labels are set for the axis, giving fontsize and ticks labels are given to axis values and fontsize.
The x_range variable is set and contains the linspace method which will add the plot of the function h(x) = x^3 which will be created next, in the range [0, 10], with 100 numbers.
The cubed function is defined in variable y. If you want to amend this cubed function to squared function for example this can be done easily by changing - y = x_range ** 2 ( and amend the label name in the code to h(x) = x^2).
The Plot function will set the cubed function, color & label.
The legend function will display the legend - the labels for histogram function as "Normal Distribution" and the cubed function as "Function h(x) = x^3".
If you want to save your plot use can do so, remove the comment to do this, plt.savefig('My_plot.png'), note ensure this function is called before the show function, otherwise if it is after the show function your image will be blank.
Display the plot using plt.show, note you will need to close out of this if you want to end and run another task.

References:

* <https://scriptverse.academy/tutorials/python-matplotlib-plot-function.html> 
* <https://www.geeksforgeeks.org/how-to-plot-normal-distribution-over-histogram-in-python/>
* <https://matplotlib.org/1.5.3/users/style_sheets.html>
* <https://numpy.org/doc/stable/reference/generated/numpy.linspace.html>
* <https://data-flair.training/blogs/numpy-applications/> 

## References and supports for creating the readmilefile
________________________________________

[Markdownguide](https://www.markdownguide.org/basic-syntax/)

[Freecodecamp](https://www.freecodecamp.org/news/how-to-write-a-good-readme-file/)

[Makeareadme](https://www.makeareadme.com/)

[dillinger](https://dillinger.io/)
