""" 
*************************************************************************************
Author: SK
Date: 23-Apr-2020
Description: Python Assignments for practice; 
    a. Accept First Name & Last name from user
    b. Print the characters of First Name & Last Name in reverse.
    c. Print characters of Last Name & First Name with a space in between.
************************************************************************************* 
"""

#function for reversing a string
def reverse(str): 
    reversedString=[]
    index = len(str) 
    while index > 0: 
        reversedString += str[ index - 1 ] 
        index = index - 1 
    return reversedString
    
    
fname= input("Enter First Name: ")
lname= input("Enter Last Name: ")

print("Last Name & First Name is: ", lname, " ", fname)


print("Reverse of First Name is: ", end="")
print(reverse(fname))
print("Reverse of Last Name is: ", end="")
print(reverse(lname))

print("Last Name & First Name in reverse: ", reverse(lname), " ", reverse(fname))
