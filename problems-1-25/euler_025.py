# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 12:28:30 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=25


# define second and third fibonacci numbers 
fibonacci_list = [1]
i = 2

# calculate next fibonacci numbers until the first that has 1000 digits
while True:
    fibonacci_list.append(i)
    if len(str(i)) == 1000:
        break
    i = fibonacci_list[-1] + fibonacci_list[-2]

# insers first fibonacci number
fibonacci_list.insert(0, 1)

# calculate length
len(fibonacci_list) 
    
