#week6
#Author: Sarah Hastings
#This program takes a positive floating-point number as input and outputs an approximation of its square root.
#This program will use the square root function - newton method
#Reference: https://www.simplilearn.com/tutorials/python-tutorial/float-in-python#:~:text=Float()%20is%20a%20method,as%20the%20floating%2Dpoint%20output. ,
            # https://thirumalai2024.medium.com/python-program-to-find-square-root-of-the-number-using-newtons-method-937c0e732756 ,
            # https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/                 

num = float(input("Please enter a positive number: "))  #User is prompted to enter a positive float number

def newtonsqrt(n):                                      #This function will callulate the squart root
    approx=0.5*n
    better=0.5*(approx+n/approx)
    while better!=approx:
        approx=better
        better=0.5*(approx+n/approx)
    return round(approx,1)
    
print(f"The square root of {num} is approx. {newtonsqrt(num)}.")  #This will call the function and print the output results
 