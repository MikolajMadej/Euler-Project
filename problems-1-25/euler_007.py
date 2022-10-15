# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 22:52:24 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=7


# 10 001 st prime number
# num = 104743

# import math library
import math


# define a function that checks is number is prime
def is_prime(num):
    for div in range(2, math.ceil(math.sqrt(num))+1):
        if num % div == 0:
            return False
    return True

# define first prime number
prime_numbers = [2]
i = 1

# calculate 10 000 further prime numbers
while True:
    i += 2
    if is_prime(i) == True:
        prime_numbers.append(i)
        
        if len(prime_numbers) == 10001:
            break
        
# print the last prime number on the list
prime_numbers[-1]

