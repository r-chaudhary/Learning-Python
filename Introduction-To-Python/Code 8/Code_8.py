# Introduction to Python
# Programmer : Rahul Chaudhary
# Email : r.chaudhary@outlook.in

# Code : 8
# Python Program to calculated String Length by loop.

def length(data):
    length = 0
    for i in data:
        length = length + 1
    return length

string = input("Enter String : ")
print("Length of %s is %d."%(string,length(string)))
