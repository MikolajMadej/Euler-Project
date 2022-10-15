# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 19:25:13 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=9


# look for pithagorean triplet assuming a+b+c = 1000
for a in range(1, 1000):
    for b in range(1, 1000):
        c = 1000 - a - b
        if c == (a*a+b*b)**(1/2): 
            break
    else:                                        # execute only when it's no break in the inner loop. 
        continue
    break

print(a*b*c)