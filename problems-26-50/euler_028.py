# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 12:26:43 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=28


# 3, 5, 7, 9 (by 2)
# 13, 17, 21, 25 (by 4)
# 31, 37, 43, 49 (by 6) 

# define length of squre side
length_of_square = 1001

# initiate list of numbers on diagonals
list_to_sum = []

# numbers on diagonals are far from each other by 2, 4, 6... for sgares 1, 2, 3 ect 
i = 1
multiplier = 1
while i < (length_of_square*length_of_square):
    i = i + 2 * multiplier
    list_to_sum.append(i)
    
    # if list is divisible by 4 (we got all 4 corners) we can move to further square which always has sides longer by 2 than the previous
    if len(list_to_sum) % 4 == 0:
        multiplier = multiplier + 1

# insert 1 at the beginning as a start point
list_to_sum.insert(0, 1)

# calculate sum of numbers on diagonals
sum(list_to_sum)
