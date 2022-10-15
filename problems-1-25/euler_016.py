# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 13:59:12 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=16

# calculate the sum of digits in 2^1000
number = 2**1000
sum(list(map(int, str(number))))