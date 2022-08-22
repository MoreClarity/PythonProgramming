# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


start = int(input("starting value? "))

end = int(input("ending value? "))

print(f'\n{"Num":<5}{"Sqr":<}')
print("-----------")
for x in range(start, end+1):
    
    sqr = x**2
    print(f'{x:<5}{sqr:<}')
    
        

