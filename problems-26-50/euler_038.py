# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 13:36:14 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=38


import numpy

# define a function that converts a list of string-numbers to a list of numbers
def convert_list_to_number(input_list):
    
    as_list_of_numbers = list(map(int, input_list))                            # convert all string-numbers to number-numbers
    as_number = int("".join(map(str, as_list_of_numbers)))                     # bind all numbers on the list to one number
    
    return as_number


# initiate max pandigital
max_pandigital = 0
max_number = 0
up_to_what = 0


# check all numbers from 1 to 9999
for integer in range(1, 10000):
    
    current_pandigital = []
    
    # integer can be multiplied by 1, 2, 3... 9
    for n in range(1, 10, 1):
        
        # calculate product
        output = list((str(integer * n)))
        
        # break if product has duplicate numbers or dupliacted numbers appear when joining product from current pandigital
        if not(len(output) == len(set(output))) or not (len(output) + len(current_pandigital)) == len(list(numpy.unique(current_pandigital + output))):
            break
        else:
        # if no duplicated integers appear, add product to current pandigital
            current_pandigital = current_pandigital + output
        
        # break when pandigital achieves or exceeded 9-length
        if len(current_pandigital) >= 9:
            break
    
    # if current pandigital does not contain 0 and is 9-digit long, check if it's greater than current max
    if len(current_pandigital) == 9 and convert_list_to_number(current_pandigital) > max_pandigital and "0" not in current_pandigital:
        max_pandigital = convert_list_to_number(current_pandigital)
        max_number = integer
        up_to_what = n
    


print(max_pandigital)

