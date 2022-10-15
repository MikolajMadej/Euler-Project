# -*- coding: utf-8 -*-
"""
Created on Sat Oct  8 11:23:39 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=21


# define a function that calculates a sum of proper divisors
def sum_of_divisors(number):
    proper_divisors = []
    for i in range(1, int((number/2+1))):
        if number % i == 0:
            proper_divisors.append(i)
    return(sum(proper_divisors))


# sum_of_divisors(sum_of_divisors(4))

# find amicable numbers (eg. d(220) = 284 and d(284) = 220 where d() is sum of proper divisors)
amicable_numbers = []
for i in range(1, 10000):
    if i == sum_of_divisors(sum_of_divisors(i)) and i != sum_of_divisors(i):
        amicable_numbers.append(i)


# print sum of amicable numbers
sum(amicable_numbers) 
