# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 12:24:54 2023

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=71

input_nominator = 3
input_denominator = 7
MAX = 1000000

# let's look for a proper frction on the left to 3/7
# let's find biggest number divisible by 7, that is also smaller than 1M

i = MAX + 1
while i % input_denominator != 0:
    i -= 1

denominator = i
print("Denominator i s equal to:", denominator)


# recalculate 3/7 to a fraction with found denominator 
ratio = int(i / input_denominator)
numerator = ratio * input_nominator

# check if this is a reduced proper fraction
def greates_common_divisor(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

GCD = greates_common_divisor(numerator, denominator)
# its not, because GCD is not equal to 1

# find the biggest nominator that gives a proper reduced fraction with 999999 denominator
while greates_common_divisor(numerator, denominator) != 1:
    numerator -= 1

print(numerator)
print("Numerator:", numerator, 
      "\nDenominator:", denominator, 
      "\nGCD:", greates_common_divisor(numerator, denominator))
