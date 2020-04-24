""" 
*************************************************************************************
Author: SK
Date: 23-Apr-2020
Description: Python Assignments for practice; 
    a. Print numbers between 2000 and 3200 (both included) which are divisble by 7
    but are not multiple of 5.
************************************************************************************* 
"""

#function for reversing a string
def reverse(string): 
    string = "".join(reversed(string)) 
    return string


userString= input("Enter a string to reverse: ")

print("Reverse of entered string is: ", end="")
print(reverse(userString))
