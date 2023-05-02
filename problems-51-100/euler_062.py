# -*- coding: utf-8 -*-
"""
Created on Sun Jan 29 16:37:21 2023

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=63

# key is a sorted string of digits in a cubic number
# value in doctionary is a list of numbers that are cubic numbers


def solve():
    
    # initaite a dictionary of "keys"
    dict_of_numbers = {}

    # start cubing numbers from 1
    i = 1
    last_len = 1
    
    while True:
        num = i**3
        
        # transfor every cubic number to it's key (sorted digits in a form of a string)
        num_to_dict = "".join(sorted(str(num)))
        
        current_len = len(num_to_dict)
        
        # if crrent key has 5 different numbers , output smalles of them
        if current_len > last_len:
            for value in dict_of_numbers.values():
                if len(value) == 5:
                    return(min(value))
            
            last_len = current_len
            dict_of_numbers = {}
  
            
        # chceck if key is in a dictionary, if not - add new element
        if num_to_dict not in dict_of_numbers.keys():
            dict_of_numbers[num_to_dict] = []
            
        # add current number to it's corresponding key    
        dict_of_numbers[num_to_dict].append(num)
            
        i += 1

    
solve()  

