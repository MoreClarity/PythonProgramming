# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
# Ryan Hodgson - CSC 121 - Python Programming
# While loops

# Create the while loop statement
# Add .lower() a method to allow a user to enter a capital and be converted to lower case

keep_going = "y"
while keep_going.lower() == "y":
    

    score = float(input("Enter score: "))
    
    #evaluate score
    
    if score >= 90:
    
        print("A")
    
    elif score >= 80:
    
        print("B")
    
    elif score >= 70:
    
        print("C")
    
    elif score >= 60:
    
        print("D")
    
    else:
    
        print("F")
        
            
    keep_going = input("Do you want to enter another score? (y for yes):" )    
