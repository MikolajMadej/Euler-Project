# -*- coding: utf-8 -*-
"""
Created on Sat Oct  1 19:47:52 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=10


import math

# define a function that returns True if a number is prime
def is_prime(num):
    for div in range(2, math.ceil(math.sqrt(num))+1):
        if num % div == 0:
            return False
    return True


# define first prime
sum_of_primes = 2

# add all next primes (below 2 million)
for i in range(2, 2000000):
    if is_prime(i):
        sum_of_primes += i


# print the output
print(sum_of_primes)