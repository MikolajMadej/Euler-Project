# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 22:26:27 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=15

# we are looking for the middle value in a 41 row of Pascal triangle (20x20 grid)
import math
x = 41
previous_row = [1]

# calculate pascal triangle
for row_id in range(2, x+1, 1):
   current_row = [0] * row_id
   for value_in_row_id in range(0, row_id):
       if (value_in_row_id == 0) or (value_in_row_id == row_id-1):
           current_row[value_in_row_id] = 1
       else: current_row[value_in_row_id] =  previous_row[value_in_row_id-1] + previous_row[value_in_row_id]
   previous_row = current_row 
   

# get the middle value of the last row
middle_value = current_row[int(math.ceil(len(current_row)/2)) - 1]
print(middle_value)           
           
       
    