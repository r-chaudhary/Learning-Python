# Introduction to Python
# Programmer : Rahul Chaudhary
# Email : r.chaudhary@outlook.in

# Code : 19
# Python Program to read last n lines form File.

def last_n_lines(file_name,num_of_lines):
    with open(file_name) as file:
        print("Last %d lines form file are "%num_of_lines)
        for line in file.readlines()[num_of_lines:]:
            print(line)

file_name = "Code_19.txt"
last_n_lines(file_name,5)
            
