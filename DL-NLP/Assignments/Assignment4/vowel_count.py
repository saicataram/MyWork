""" 
*************************************************************************************
Author: SK
Date: 30-Apr-2020
Description: Python Assignments for practice; 
    a. Count no of vowels in the provided string.
************************************************************************************* 
"""

def vowel_count(str): 
      
    # Initializing count variable to 0 
    count = 0
      
    # Creating a set of vowels 
    vowel = set("aeiouAEIOU") 
      
    # Loop to traverse the alphabet 
    # in the given string 
    for alphabet in str: 
      
        # If alphabet is present 
        # in set vowel 
        if alphabet in vowel: 
            count = count + 1
      
    print("No. of vowels :", count)

str = input("Enter a character: ")
  
# Function Call 
vowel_count(str)