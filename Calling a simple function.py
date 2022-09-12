# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

 
def main():
    
    pay_rate, hours_worked = get_info()

 # Calculate gross pay
     
    gross_pay = pay_rate * hours_worked 
    print("Your gross pay is: " , gross_pay)

# Create a function to get pay info 
    
def get_info():
    pay_rate = float(input("Enter your pay rate? "))
    hours_worked = float(input("Enter your hours worked: "))
    
    return pay_rate, hours_worked
    

main()



    
    