# Introduction to Python
# Programmer : Rahul Chaudhary
# Email : r.chaudhary@outlook.in

# Code : 17
# Python Program to demonstrate Reading of File.

file = open("Code_17.txt",'r')
print("File readline    : ",file.readline())
print("File read        : ",file.read(9))
print("File readline(9) : ",file.readline(9))
file.seek(0)
print("File readline(9) : ",file.readline(9))
file.seek(0)
print("File readline    : ",file.readlines())
file.seek(0)
print("File Data        : \n",file.read())
file.close()
