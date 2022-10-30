# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 12:56:38 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=37


import math

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


# initite list of truncatable primes
truncatable_primes = []

# while loop will iterate by 2 starting from 11 to look for truncatableprimes
number = 11


while len(truncatable_primes) < 11:
    
    number_copy_dfr = number                                                   # delete from right
    number_copy_dfl = number                                                   # delete from left

    # start with assumption number is a truncatable prime
    truncatable_dfr = True
    truncatable_dfl = True

    # if any subnumber (deleting starting from right) is not a prime, output False
    for digit in range(len(str(number))):
        if not is_prime(number_copy_dfr):
            truncatable_dfr = False
        number_copy_dfr = number_copy_dfr // 10                                # floor division: 345 // 10 = 34


    # if any subnumber (deleting starting from left) is not a prime, output False
    for digit in range(len(str(number))):
        if not is_prime(number_copy_dfl):
            truncatable_dfl = False
        number_copy_dfl = (number_copy_dfl % (10**(len(str(number)) - digit - 1)))  # division rest: 345 % 10**(3-0-1) = 45
    
    if truncatable_dfr & truncatable_dfl:
        truncatable_primes.append(number)
    number += 2
    
    
print(sum(truncatable_primes))