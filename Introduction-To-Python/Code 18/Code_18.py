# Introduction to Python
# Programmer : Rahul Chaudhary
# Email : r.chaudhary@outlook.in

# Code : 18
# Python Program to demonstrate Writing of File.

file = open("Code_18.txt",'a')
file.write("My name is Rahul \nI am doing python \nCool Cool Cool")
file.close()

file = open("Code_18.txt",'r')
data =  file.readlines()
for i in data:
    print(i)
file.close()
