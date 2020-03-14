# Introduction to Python
# Programmer : Rahul Chaudhary
# Email : r.chaudhary@outlook.in

# Code : 4
# Python Program to Reverse a Number.

def reverse(number):
    rev = 0
    while number > 0:
        rem = number % 10
        rev = (rev * 10) + rem
        number = number // 10
    return rev

num = int(input("Enter number : "))
print("Reverse of %d is %d"%(num,reverse(num)))
