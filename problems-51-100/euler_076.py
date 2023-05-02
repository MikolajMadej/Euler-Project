# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 20:38:52 2023

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=76

objective = 100
ways = [0]*objective
ways.insert(0, 1)

for x in range(1, objective):
    for i in range(x, objective+1):
        ways[i] = ways[i] + ways[i-x]

print(ways[objective])

