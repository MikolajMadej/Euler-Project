# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 17:21:41 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=52

# First number to contain the same digits is 142857


i = 1
assumption = True

while True:
    for j in range(1, 7):
        if sorted(str(i*j)) != sorted(str(i)):                # sorted() gives all digits of a string sorted 
            assumption = False
            break
        else:
            assumption = True

    if assumption == True:
        print(i)
        break
    i +=1
    
    