# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 13:12:00 2023

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=64

# based on https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion

BOUND = 10000

n = 8

# function to calculate the continued fraction
def count_period(n):
    mn = 0
    dn = 1
    
    a0 = int((n)**(1/2))   # calculate the "first guess" so the integer part of numbers' square root
    an = int((n)**(1/2))   # initiate the integer part of the reminder
    
    period = 0             # function will return period = 0 if square root is an integer
    # print(a0)
    
    if a0 != (n**(1/2)):               # function will calculate the length of period if sqrt is not an integer
        while an != 2*a0:              # period starts repeating if an is equal to 2 x a0
            mn = dn*an - mn
            dn = (n - mn**2)/dn
            an = int((a0 + mn)/dn)
            # print(an)
            period += 1
    return period

# count_period(23)
# initiate counter
counter = 0

# loop from 0 to max bound and check if period is even
for i in range(BOUND + 1):
    if count_period(i) % 2 != 0:
        counter += 1

# print the result
print(counter)

