# Introduction to Python
# Programmer : Rahul Chaudhary
# Email : r.chaudhary@outlook.in

# Code : 3
# Python Program to demonstrate Fibonacci Series.

limit = int(input("Enter range : "))
num1 = 0
num2 = 1
print(num1 ,end = " ")
print(num2 ,end = " ")
for i in range(limit-2):
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    print(num3 ,end = " ")
