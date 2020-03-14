# Introduction to Python
# Programmer : Rahul Chaudhary
# Email : r.chaudhary@outlook.in

# Code : 24
# Python Program to demonstrate Object Oriented Programming.

class Number:
    MULTIPLIER = 35
    def __init__ (self,x,y):
        self.x = x
        self.y = y
    def add(self):
        return self.x + self.y
    def multi(a):
        return Number.MULTIPLIER * a
    def sub(b,c):
        return b - c
    def value(self):
        return (self.x ,self.y)
    def set_value(self, x, y):
        self.x = x
        self.y = y
    def _value(self,x,y):
        self.x = x
        self.y = y

S = Number(10,20)
print("ADD :",S.add())
print("MULTIPLY :",Number.multi(10))
print("SUB :",Number.sub(10,9))
print("Value :",S.value())
S.set_value(20,30)
print("NEW VALUE",S.value())
