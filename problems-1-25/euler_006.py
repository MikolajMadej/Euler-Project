# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 12:33:14 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=6

# calculate the square of sum of first 100 numbers 
a = (sum(list(range(1,101))))**2


# define the function which calculates the square of every number on given list
def power(input_list):
    return [x**2 for x in input_list]


# apply the function on list 1-100
b = sum(power(list(range(1,101))))


# print the difference
print(a-b)