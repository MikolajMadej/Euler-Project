# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 21:07:12 2023

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=97

# number to big to assign
# number = 1 + 28433 * 2**7830457

# needs to be calculated iteratively
n = 2

for i in range(7830457 - 1):
    n = (n * 2) % 10000000000
    
n = (n * 28433 + 1) % 10000000000
print(n)