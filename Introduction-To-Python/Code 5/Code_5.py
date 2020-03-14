# Introduction to Python
# Programmer : Rahul Chaudhary
# Email : r.chaudhary@outlook.in

# Code : 5
# Python Program to check whether it is Armstrong and Palindrome Number.

def reverse(number):
    rev = 0
    while number > 0:
        rem = number % 10
        rev = (rev * 10) + rem
        number = number // 10
    return rev

def armstrong(num):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp = temp // 10
    if num == sum:
        print("%d is an Armstrong number "%num)
    else:
        print("%d is not an Armstrong number "%num)

def palindrome(num):
    if num == reverse(num):
        print("%d is an palindrome number "%num)
    else:
        print("%d is not an palindrome number "%num)

num = int(input("Enter number : "))
armstrong(num)
palindrome(num)
