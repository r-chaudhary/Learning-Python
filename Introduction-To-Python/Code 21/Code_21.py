# Introduction to Python
# Programmer : Rahul Chaudhary
# Email : r.chaudhary@outlook.in

# Code : 21
# Python Program to demonstrate Single Inheritance.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getInfo(self):
        return self.name + " " + str(self.age)

    def isEmployee(self):
        print("Employee ",end="")
        return False

class Employee(Person):
   def isEmployee(self):
        print("Employee ",end="")
        return True

p=Person("RAHUL",19)
print(p.getInfo())
print(p.isEmployee())

emp=Employee("RAHUL",20)
print(emp.getInfo())
print(emp.isEmployee())
