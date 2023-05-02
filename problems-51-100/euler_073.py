# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 16:33:07 2023

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=73


MAX = 12000
count = 0

# implement greatest common divisor
def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

# chceck if proper fraction is between 1/3 and 1/2
# count it if it is
for denominator in range(MAX + 1):
    for numerator in range(denominator):
        
        if numerator/denominator > 1/3 and  \
           numerator/denominator < 1/2 and  \
           gcd(numerator, denominator) == 1:
           count += 1 

# print the solution            
print(count)


# gcd(98, 21)
# 98, 21
# 21, 14
# 14, 7
# 7, 0
