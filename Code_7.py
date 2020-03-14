# Introduction to Python
# Programmer : Rahul Chaudhary
# Email : r.chaudhary@outlook.in

# Code : 7
# Python Program to check character is vowel.

def check_vowel(char):
    vowel_list = ['a','e','i','o','u']
    if char.lower() in vowel_list:
        return True
    return False

char = input("Enter Character : ")
print(check_vowel(char))

