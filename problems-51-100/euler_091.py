# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 14:39:03 2023

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=91

# set the limit
limit = 50

# Test if the three points {(0,0), (x1,y1), (x2,y2)} form a right triangle.
def is_right_triangle(x1, y1, x2, y2):
    # a is a second power of length of one of the sides
    a = x1**2 + y1**2                      
                   
	 # b is a second power of length of other one of the sides
    b = x2**2 + y2**2
    
    # b is a second power of length of other one of the sides
    c = (x2 - x1)**2 + (y2 - y1)**2
     
    return (a + b == c) or (b + c == a) or (c + a == b)

# initiate count
count = 0

# check all locations for the two points
for x1 in range(limit + 1):
    for y1 in range(limit + 1):
        for x2 in range(limit + 1):
            for y2 in range(limit + 1):
            		# For uniqueness, ensure that (x1,y1) has a larger angle than (x2,y2)

                if is_right_triangle(x1, y1, x2, y2) and y2 * x1 < y1 * x2 :
                    count += 1
    
print(count)
