""" 
*************************************************************************************
Author: SK
Date: 30-Apr-2020
Description: Python Assignments for practice; 
    a. Validate the character entered by users whether it is vowel or consonant.
************************************************************************************* 
"""

ch = input("Enter a character: ")

if(ch=='A' or ch=='a' or ch=='E' or ch =='e' or ch=='I'
 or ch=='i' or ch=='O' or ch=='o' or ch=='U' or ch=='u'):
    print(ch, "is a Vowel")
else:
    print(ch, "is a Consonant")

