#week6
#Author: Sarah Hastings
#This program takes a positive floating-point number as input and outputs an approximation of its square root.
#square root function - newton method


num = float(input("Please enter a positive number: "))

def newtonsqrt(n):
    approx=0.5*n
    better=0.5*(approx+n/approx)
    while better!=approx:
        approx=better
        better=0.5*(approx+n/approx)
    return round(approx,1)
    #return(approx)
print(f"The square root of {num} is approx. {newtonsqrt(num)}.")
#print(f"The square root of {num} is approx. {math.sqrt.round(num,1)} ")
#print(newtonsqrt(16))