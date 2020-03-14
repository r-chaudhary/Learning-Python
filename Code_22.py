# Introduction to Python
# Programmer : Rahul Chaudhary
# Email : r.chaudhary@outlook.in

# Code : 22
# Python Program to demonstrate Multi-Level Inheritance.
class Person:
   def __init__(self,name,age):
      self.name=name
      self.age=age

   def getInfo(self):
      return(self.name+ " " + str(self.age))
   
   def isEmployee(self):
      return False
    
class Employee(Person):
   def isEmployee(self):
      return True
   
   def isGovernment(self):
      return False


class Government(Employee):
   def isGovernment(self):
      return True

p=Person("RAHUL-COOL",10)
print(p.getInfo())
print(p.isEmployee())

emp=Employee("RAHUL-COOL_AGAIN",20)
print(emp.getInfo())
print(emp.isEmployee())
print(emp.isGovernment())

g=Government("COOL_RAHUL_COOL_",30)
print(g.getInfo())
print(g.isEmployee())
print(g.isGovernment())
