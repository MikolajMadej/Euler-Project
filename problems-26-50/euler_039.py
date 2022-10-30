# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 14:38:04 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=39


# smallest right angle triangle is 3-4-5 (total length of 12)


import math

# initiate max number of solution and a variable that hold info for total triangle sides lengths that gives this max number of solutions
max_number_of_solutions = 0
best_length = 0 

# iterate through all possible side length sums starting from 12 to 1000
for tot_length in range(12, 1001):
    
    current_number_of_solutions = 0
    
    # one of the sides is by definition between 1/3 and 1/2 of total side-length
    min_a = math.floor(tot_length/3)
    max_a = math.floor(tot_length/2)

    for a in range(min_a, max_a, 1):
        
        for b in range(1, tot_length + 1 - a):
            
            c = tot_length - a - b
            
            if a**2 + b**2 == c**2:
                current_number_of_solutions += 1
    
    if current_number_of_solutions > max_number_of_solutions:
        max_number_of_solutions = current_number_of_solutions
        best_length = tot_length


print(max_number_of_solutions)
print(best_length)
