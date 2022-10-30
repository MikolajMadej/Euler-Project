# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 12:06:16 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=27


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


# initiate variables for max number of consecutive primes and a and b that create them
max_num_of_primes = 0
a_max = 0
b_max = 0


# traverse through all a and be between -1000 and 1000 
for a in range(-1000, 1000, 1):
    for b in range(-1001, 1001, 1):
        
        n = 0
        while is_prime(n**2 + n*a + b):
            n += 1
        
        if n > max_num_of_primes:
            max_num_of_primes = n
            a_max = a
            b_max = b
            
  # print a and b for quadratic formula that gives max number of consecutive primes          
print(a_max*b_max)
