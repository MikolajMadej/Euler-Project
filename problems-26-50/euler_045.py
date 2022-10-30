# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 10:48:22 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=45


# implement 3 finctions that check if number is triangle/pentagonal/hexagonal (functions copied from previous problems)
import math 


# define a function that checks if number is triangle
def is_triangle(number):
    if math.ceil(math.sqrt(8 * number + 1)) == math.floor(math.sqrt(8 * number + 1)):
        return True
    else:
        return False


# define a function that checks if number is pentagonal
def is_pentagonal(number):
    inverse = (math.sqrt(1 + 24 * number) + 1) / 6
    if inverse == int(inverse):
        return True
    else: 
        return False

# define a function that checks if number is hexagonal
def is_hexagonal(number):
    if math.ceil((1 + math.sqrt(8 * number + 1)) / 4) == math.floor((1 + math.sqrt(8* number + 1)) / 4):
        return True
    else: 
        return False
    
    
    
    
# start iterating from first number that is all triangle/pentagonal/hexagonal
i = 144
while True:
    number = i * (2*i-1)

    if is_triangle(number) and is_pentagonal(number) and is_hexagonal(number):
        print(number)
        break
    i += 1
    