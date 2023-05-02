# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 16:02:13 2023

@author: Mikolaj Madej
"""
# Problem link
# https://projecteuler.net/problem=85

# equation for number of squares in a n x m square taken from Wikipedia:
# https://en.wikipedia.org/wiki/Triangular_number
# x = 1/2 * n * (n+1) * 1/2 * m * (m+1)

# import math
import math

# set boundaries
MAX    = 2000000
DIFF   = 2000000
NUM_N  = 0
NUM_M  = 0


# check every n and m, with two asumptions:
# 1) m >= n (always true)
# 2) n, m < sqrt(MAX) to shorten the compilation. For m = sqrt(MAX) and n >= 2 output is always > 2000000

for n in range(int(math.sqrt(MAX)) + 1):
    for m in range(n, int(math.sqrt(MAX)) + 1):
        output = 1 / 4 * n * m * (n + 1) * (m + 1)
        diff = abs(MAX - output)
        if diff < DIFF:
            DIFF = diff
            NUM_N = n
            NUM_M = m
        
        
print(NUM_N * NUM_M)

