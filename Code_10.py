# Introduction to Python
# Programmer : Rahul Chaudhary
# Email : r.chaudhary@outlook.in

# Code : 10
# Python Program to check whether string is Pangram.

def pangram(stirng):
    alpha = []
    for i in string.lower():
        if i not in alpha:
            alpha.append(i)
    if len(alpha) < 26:
        print("%s is not an pangram"%string)
    else:
        print("%s is an pangram"%string)

string = input("Enter String : ")
pangram(string)
