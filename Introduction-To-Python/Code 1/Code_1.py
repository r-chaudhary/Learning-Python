# Introduction to Python
# Programmer : Rahul Chaudhary
# Email : r.chaudhary@outlook.in

# Code : 1
# Python Program to calculate in which year user will turn 100. 

import datetime
name = input("Enter your name : ")
age = int(input("Enter your age : "))
current_time = datetime.datetime.now()
hundred_year = (current_time.year - age) + 100
print("%s will turn 100 years in %d year"%(name,hundred_year))
