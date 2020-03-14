# Introduction to Python
# Programmer : Rahul Chaudhary
# Email : r.chaudhary@outlook.in

# Introduction to Python
# Programmer : Rahul Chaudhary
# Email : r.chaudhary@outlook.in

# Code : 25
# Python Program to demonstrate Tkinter.

from tkinter import *
def display():
    label = Label(root,text="")
    label.config(text="COOOOOOOOOOOOL ......",fg="red")
    label.config(font = "times",bd=28)
    label.pack()


root = Tk()
b = Button(root,text="View Effect",command=display)
b.pack()
b.mainloop()