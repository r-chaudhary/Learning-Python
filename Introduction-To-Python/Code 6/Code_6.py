# Introduction to Python
# Programmer : Rahul Chaudhary
# Email : r.chaudhary@outlook.in

# Code : 6
# Python Program to calculate Factorial by Recursion.

def recursive_factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num*recursive_factorial(num - 1)

num = int(input("Enter number : "))
print("Factorial of %d is %d "%(num,recursive_factorial(num)))
