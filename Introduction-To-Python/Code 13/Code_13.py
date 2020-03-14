# Introduction to Python
# Programmer : Rahul Chaudhary
# Email : r.chaudhary@outlook.in

# Code : 13
# Python Program to remove 1, 3, 5, 6 element from list.

def create_list():
    len = int(input("Enter list length [>6] : "))
    if len < 6:
        exit()
    list = []
    for i in range(len):
        list.append(int(input("Enter Number : ")))
    return list

list_1 = create_list()
list_2 = [list_1[0] , list_1[2], list_1[4], list_1[5]]

for i in list_2:
    if i in list_1:
        list_1.remove(i)

print("LIST : ",list_1)
