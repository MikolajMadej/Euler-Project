# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 13:50:15 2023

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=65


# initiate exponent continued fraction
e = [2,]

# iterator
i = 1

# while loop to fill continued fraction with 100 next numbers
while len(e) < 100:   
    e = e + [1, 2*i, 1]
    i += 1
    
# reverse the list
e_rev = e[::-1]
    
# initiate numerator
numerator = 1
# initiate denominator 
denominator = e_rev.pop(0)

# calculate numerator and enominator for 100th fraction
for i in e_rev:
    numerator = i * denominator + numerator
    
    # instead of temp, we can use doubble assignment at the same time using ,
    numerator_temp = numerator
    denominator_temp = denominator
    
    denominator = numerator_temp
    numerator = denominator_temp
    
# final switch
fin_numerator = denominator
fin_denominator = numerator

# calculate sum of digits in numerator
print(sum(int(digit) for digit in str(fin_numerator)))




