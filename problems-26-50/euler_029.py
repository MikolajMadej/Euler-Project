# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 13:32:54 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=29


# initiate the list of dictinct terms
distinct_terms = []


# if a to power b gives distinct number, append it
for a in range(2, 101):
    for b in range(2, 101):
        if a**b not in distinct_terms:
            distinct_terms.append(a**b)
            
# sort the list
distinct_terms.sort()  

# print length of the list
print(len(distinct_terms))

