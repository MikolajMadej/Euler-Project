# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 21:11:13 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=44


import math 

# define a function that checks if number is pentagonal
# inverse function for pentagonal numbers taken from https://en.wikipedia.org/wiki/Pentagonal_number
def is_pentagonal(number):
    inverse = (math.sqrt(1 + 24 * number) + 1) / 6
    if inverse == int(inverse):
        return True
    else: 
        return False


# check all pentagonal numbers until condition is met
i = 7
j = 4
while True:
    current_penthagonal = int(i * (3 * i - 1) / 2)
    
    for j in range(i - 1, 1, -1):
        other_penthagonal = int(j * (3 * j - 1) / 2)
        
        if is_pentagonal(current_penthagonal - other_penthagonal) and is_pentagonal(current_penthagonal + other_penthagonal):
            break
    
    # use same if statement as above to break out of whe outer loop as well
    if is_pentagonal(current_penthagonal - other_penthagonal) and is_pentagonal(current_penthagonal + other_penthagonal):
        print(current_penthagonal - other_penthagonal)
        break    
    
    i += 1
    
    
# PLEASE NOTE: this solution finds the first number that meets conditions:
# 1) Pj - Pk is pentagonal
# 2) Pj + Pk is pentagonal

# first found solution happens to also meet the third condition:
# 3)  D = |Pk − Pj| is minimised

# why?   
#  P(2)-P(1) = 4
#  P(3)-P(2) = 7
#  P(4)-P(3) = 10 
# so P(n)-P(n-1) < P(n+1)-P(n) < P(n+2)-P(n+1) ...
# This means the difference between adjacent terms is increasing. And also, for the nth term, the minimum D, even without the condition, will be
