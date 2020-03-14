# Introduction to Python
# Programmer : Rahul Chaudhary
# Email : r.chaudhary@outlook.in

# Code : 15
# Python Program to demonstrate concatenation of Dictionary.

dict_1 = {1:10,2:20}
dict_2 = {3:30,4:40}
dict_3 = {5:50,6:60}
dict_4 = {}
dict_5 = {}

#Method number 1 for concatenating dictionary
for key, value in dict_1.items():
    dict_4[key] = value
for key, value in dict_2.items():
    dict_4[key] = value
for key, value in dict_3.items():
    dict_4[key] = value
print("Concatinated Dictionary : ",dict_4)

#Method number 2 for concatenating dictionary

dict_5.update(dict_1)
dict_5.update(dict_2)
dict_5.update(dict_3)

print("Concatinated Dictionary : ",dict_5)
