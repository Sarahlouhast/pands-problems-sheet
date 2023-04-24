#Weekly task 06
#Author: Sarah Hastings
#This program takes a positive floating-point number as input and outputs an approximation of its square root.
#This program will use the square root function - newton method
#References:  https://www.simplilearn.com/tutorials/python-tutorial/float-in-python#:~:text=Float()%20is%20a%20method,as%20the%20floating%2Dpoint%20output. ,
            # https://thirumalai2024.medium.com/python-program-to-find-square-root-of-the-number-using-newtons-method-937c0e732756 ,
            # https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/ , 
            # https://towardsdatascience.com/newton-raphson-explained-and-visualised-23f63da21bd5 ,
            # https://runestone.academy/ns/books/published/thinkcspy/MoreAboutIteration/NewtonsMethod.html ,
            # https://towardsdatascience.com/develop-your-own-newton-raphson-algorithm-in-python-a20a5b68c7dd 


num = float(input("Please enter a positive number: "))            #The user is prompted to enter a positive floating point numnber.

def newtonsqrt(n, tolerance=1e-10):                               #The square root function is defined using the Newton-Raphson method, which has two parameters it will take in, a number and a tolerance, the tolerance is used to get accuracy
                                                                  #Note the tolerance here is set to 1e-10 which is 1 multiplied by 10 to the power of -10, which is 0.0000000001, the function will continue to check the approx value until the difference between the current approx and the true square root is very small, up to a precision of 10 decimal places.                                                      
    approx=0.5*n                                                  #Start with any approximation, half of the input number                                     
    better=0.5*(approx+n/approx)                                  #Compute a better approximation using this formula
    while abs(better - approx) > tolerance:                       #Adding the while loop to check if the difference between better and approx is greather than the tolerance value, in this case comparing the absolute difference between better and approx to the tolerance value of 1e-10, the loop will stop when the difference is less than the tolerance level          
        approx=better                                             #Within this loop, approx is updated to the value of better
        better=0.5*(approx+n/approx)                              #Next better is updated to the new approx value using this formula
    return round(approx,1)
    
print(f"The square root of {num} is approx. {newtonsqrt(num)}.")  #This will call the function and print the output results  


