# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 14:19:22 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=56

# initiate max sum of digits
max_sum = 0


# check sum of digits for every a**b
for a in range(1, 101, 1):
    for b in range(1, 101, 1):
        number = a**b
        sum_of_digits = sum(map(int, list(str(number))))
        
        if sum_of_digits > max_sum:
            max_sum = sum_of_digits
            
# print max sum of digits
print(max_sum)
