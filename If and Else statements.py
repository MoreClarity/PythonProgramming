# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Evaluate if client qualifies for loan
# two conditions ( >=$30000 and employed for >=2 years)

salary = float(input("Enter annual income please: ")) 

# Evaluate length of employment

if salary >= 30000 :
    
    # ask for years worked
    
    years = float(input("Enter years worked please: "))
    
    if years >= 2:
        
        expenses = float(input("Enter monthly expenses please: "))
        
        annual_expenses = expenses * 12
        
        ten_percent = salary * .1
        
        if annual_expenses < ten_percent:
            
            print("approved")
        else:
            
            print("You spend too much")
        
        
        
    else:
    
        # If employment time not 2 years of less you will not qualify
        
        print("You haven't worked for 2 or more years")
        
else:
    
    print("you don't qualify, your income is too low")

