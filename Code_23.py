# Introduction to Python
# Programmer : Rahul Chaudhary
# Email : r.chaudhary@outlook.in

# Code : 23
# Python Program to demonstrate Multiple Inheritance.

class A:
    def __init__(self):
        self.str1 = "COOL"
        print("Base Class A")

class B:
    def __init__(self):
        self.str2 = "COOL BRO"
        print("Base Class B")

class C(A,B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        print("Derived Class C")

    def show(self):
        print(self.str1,self.str2)

obj = C()
obj.show()
