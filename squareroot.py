#Weekly tak 06
#Author: Sarah Hastings
#This program takes a positive floating-point number as input and outputs an approximation of its square root.
#This program will use the square root function - newton method
#Reference: https://www.simplilearn.com/tutorials/python-tutorial/float-in-python#:~:text=Float()%20is%20a%20method,as%20the%20floating%2Dpoint%20output. ,
            # https://thirumalai2024.medium.com/python-program-to-find-square-root-of-the-number-using-newtons-method-937c0e732756 ,
            # https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/ , 
            # https://towardsdatascience.com/newton-raphson-explained-and-visualised-23f63da21bd5 , https://runestone.academy/ns/books/published/thinkcspy/MoreAboutIteration/NewtonsMethod.html 


num = float(input("Please enter a positive number: "))  #User is prompted to enter a positive float number

def newtonsqrt(n):                                      #This function will calculate the squart root using newton's method
    approx=0.5*n                                        #Start with any approximation 
    better=0.5*(approx+n/approx)                        #Compute a better approximation
    while better!=approx:                               #Adding the while condition here to execute until the approximation is no longer changing
        approx=better
        better=0.5*(approx+n/approx)
    return round(approx,1)
    
print(f"The square root of {num} is approx. {newtonsqrt(num)}.")  #This will call the function and print the output results
 