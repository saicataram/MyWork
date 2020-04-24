""" 
*************************************************************************************
Author: SK
Date: 23-Apr-2020
Description: Python Assignments for practice; 
    a. Print numbers between 2000 and 3200 (both included) which are divisble by 7
    but are not multiple of 5.
************************************************************************************* 
"""

rows = input("Enter number of asteriks pattern to be displalyed: ")
rows = int (rows)

for i in range (0, rows):
    for j in range(0, i + 1):
        print("*", end=' ')
    print("\r")

for i in range (rows, 0, -1):
    for j in range(0, i -1):
        print("*", end=' ')
    print("\r")
