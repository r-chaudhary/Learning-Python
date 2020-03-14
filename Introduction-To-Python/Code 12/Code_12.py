# Introduction to Python
# Programmer : Rahul Chaudhary
# Email : r.chaudhary@outlook.in

# Code : 12
# Python Program to print True if any list element matches to another list.

def create_list():
    len = int(input("Enter list length  : "))
    list = []
    for i in range(len):
        list.append(int(input("Enter Number : ")))
    return list

list_1 = create_list()
list_2 = create_list()

for i in list_1:
    if i in list_2:
        print("True")
        break
    
