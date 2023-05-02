# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 14:25:06 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=57

# define first square root convergent numerator and denominator
numerator = 3
denominator = 2

# initiate count of convergents where numerator has more digits than denominator 
count = 0

# check first 1000 convergents
for i in range(1, 1001, 1):
    
    # every next denominator is a sum of previous numerator and denominator
    denominator = numerator + denominator
    
    # every next numerator is a doubble current denominator minus previous numerator
    numerator = 2 * denominator - numerator
    
    if len(str(numerator)) > len(str(denominator)):
        count += 1
        
        
print(count)