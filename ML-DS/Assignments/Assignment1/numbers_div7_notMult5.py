""" 
*************************************************************************************
Author: SK
Date: 23-Apr-2020
Description: Python Assignments for practice; 
    a. Print numbers between 2000 and 3200 (both included) which are divisble by 7
    but are not multiple of 5.
************************************************************************************* 
"""

output=[]
for number in range(2000, 3200):
    if (number%7==0) and (number%5==0):
        output.append(str(number))
print (','.join(output))

