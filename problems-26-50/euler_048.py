# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 11:10:54 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=48


# initiate a sum of selfpowers
number = 0

# add all self-powers rom 1 to 1000
for i in range(1, 1001):
    number = number + i**i
    
# print their last 10 digits
print(str(number)[-10:])
