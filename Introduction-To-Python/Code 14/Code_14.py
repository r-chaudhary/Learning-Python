# Introduction to Python
# Programmer : Rahul Chaudhary
# Email : r.chaudhary@outlook.in

# Code : 14
# Python Program to sort dictionary values in Ascending and Descending Order.

y=dict()
len_Of_dict=int(input("Enter the length of dictonary : "))
for i in range(0,len_Of_dict):
         print('The element for key : ',i)
         element=input("")
         y[i]=element
print(y)
l=list(y.values())
l.sort()
print("ASCENDING order is :",l)


l=list(y.values())
l.sort(reverse=True)
print("DESCENDING order is :",l)
