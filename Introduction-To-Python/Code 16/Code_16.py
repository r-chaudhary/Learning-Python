# Introduction to Python
# Programmer : Rahul Chaudhary
# Email : r.chaudhary@outlook.in

# Code : 16
# Python Program to calculate sum of values of Dictionary.

y = dict()
len = int(input("Enter length : "))
sum = 0
for i in range(len):
    print("Enter Element for Key : ",i)
    y[i] = int(input("Enter Value : "))
    sum = sum + y[i]

print("Dictionary : ",y)
print("Sum of values : ",sum)
