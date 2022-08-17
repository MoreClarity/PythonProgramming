# -*- coding: utf-8 -*-
"""
Created on Wed Aug 17 14:31:16 2022

@author: hodgsonr3396
"""

# Ryan Hodgson & Group

# Ask the user to enter the first and second color

user_color1 = input("What is the first color? (red, blue, or green): ")
user_color2 = input("What is the second color? (red, blue, or green): ")


#1
if user_color1 == "red":
    if user_color2 == "blue":
        print("Your color is magenta")
    elif user_color2 == "green":
        print("Your color is yellow")
#2
elif user_color1 == "blue":
    if user_color2 == "green":
        print("Your color is cyan")
    elif user_color2 == "red":
        print("Your color is magenta")
#3
elif user_color1 == "green":
    if user_color2 == "blue":
        print("Your color is cyan")
    elif user_color2 == "red":
        print("Your color is yellow")

    
  