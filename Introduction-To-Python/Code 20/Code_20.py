# Introduction to Python
# Programmer : Rahul Chaudhary
# Email : r.chaudhary@outlook.in

# Code : 20
# Python Program to demonstrate Object Oriented Programming.

class Student:
    def __init__(self):
        self.r  = None
        self.n  = None
        self.g  = None

    def getInfo(self):
        self.r = int(input("Enter Rollno :"))
        self.n = input("Enter your name : ")
        self.g = int(input("Enter the GRNO : "))

    def display(self):
        print("Rollno : ",self.r)
        print("Name : ",self.n)
        print("GRNO : ",self.g)

S = Student()
S.getInfo()
S.display()


        
