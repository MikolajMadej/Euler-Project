# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 21:55:48 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=1


import numpy

# define empty list and append all multiples of 3 below 1000 
i_list = []
for i in range(3, 1000, 3):
    i_list.append(i)
    
# append all multiples of 5 below 1000
for i in range(5, 1000, 5):
    i_list.append(i)

# take unique (eg. 15, 30 are duplicated on the list) and calculate sum of elements
sum(numpy.unique(i_list))



