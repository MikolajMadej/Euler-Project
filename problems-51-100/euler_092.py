# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 17:58:25 2023

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=92

max_bound = 10000000

# check if at any point the algorithm returns either 1 or 89 (only possibilities)
def how_it_ends(n):
    
    if n == 1:
        return False
    elif n == 89:
        return True
    
    while n not in [1, 89]:
        digits = list(map(int, list(str(n))))
        squares = list(map(lambda x:pow(x, 2), digits))
        n = sum(squares)

        if n == 1:
            return False
        elif n == 89:
            return True
        
# initiate count
ends_with_89 = 0

# check all starting points upt to 10 mln
for i in range(1, max_bound):
    output = how_it_ends(i)
    
    if output:
        ends_with_89 += 1
    else: continue

# print the result
print(ends_with_89)




