# Introduction to Python
# Programmer : Rahul Chaudhary
# Email : r.chaudhary@outlook.in

# Code : 9
# Python Program to display Histogram of a List.

def create_list():
    len = int(input("Enter list length  : "))
    list = []
    for i in range(len):
        list.append(int(input("Enter Number : ")))
    return list
    
def histogram(list):
    print("----- HISTROGRAM -----")
    
    for i in list:
        print(' | ','*'*i)

list = create_list()

histogram(list)
