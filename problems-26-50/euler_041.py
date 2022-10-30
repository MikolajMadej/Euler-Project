# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 16:07:46 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=41


# Code below can be run for '123456789' and '12345678' but doesn't find any primes
# The first prime it finds is for 1-7 pandigital

import math


# import the permutations method and create all pandigitals
from itertools import permutations
all_pandigitals = list(permutations('1234567'))


# define a function that returns True if a number is prime
def is_prime(num):
    
    # edge condition - 2 is prime
    if num == 2:
        return True
    
    # numbers below 2 (esp. negative ones) are not prime
    elif num < 2:
        return False
    
    for div in range(2, math.ceil(math.sqrt(num))+1):
        if num % div == 0:
            return False
        
    return True


# reverse the list of pandigitals
reverse_pandigitals = all_pandigitals[::-1]


# for every permutation - transform tuple to integer and check if prime
for current_pandigital in reverse_pandigitals:
    
    current_number = ""
    
    for i in range(0, 7):
        current_number = current_number + current_pandigital[i]
        
    current_number = int(current_number)
   
    if is_prime(current_number):
        break

# print the first prime found
print(current_number)






