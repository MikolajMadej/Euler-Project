# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 21:20:56 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=32


# to get 9 digits in total we can multiply 4 digit number by 1 digit number or 2 digit number by 3 digit number

product_list = []

# 1 digit number times 4 digit number
for x in range(1, 10):
    for y in range(999, 10000):
        
        x_list = list(str(x))
        y_list = list(str(y))
        z_list = list(str(x*y))
        full_list = x_list + y_list + z_list 
        
        # set is a collection which is unordered, unindexed and also contains unique elements
        if (len(set(full_list)) == len(full_list) == 9) & (x*y not in product_list) & ('0' not in full_list):
            product_list.append(x*y)
    
           
    
# 3 digit number times 2 digit number        
for x in range(99, 1000):
    for y in range(9, 100):
        
        x_list = list(str(x))
        y_list = list(str(y))
        z_list = list(str(x*y))
        full_list = x_list + y_list + z_list 
        
        # set is a collection which is unordered, unindexed and also contains unique elements
        if (len(set(full_list)) == len(full_list) == 9) & (x*y not in product_list) & ('0' not in full_list):
            product_list.append(x*y)

sum(product_list)


