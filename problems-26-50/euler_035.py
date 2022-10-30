# -*- coding: utf-8 -*-
"""
Created on Sat Oct 22 14:40:19 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=35


import math
import numpy


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


# define a function that circulates a number and if all circular elements are primes, returns them as a list
def circulate(num):
    
    # initiate empty output list and desired length of this list (length of number is also a number of itc circulating variants
    circular_list = []
    length = len(str(num))
    
    # circulate the number by taking rest from division by 10, putting it in the first place and
    # adding the rest (rest is defined as all digits of the number except for the last one)
    for i in range(length):
        rem = num % 10
        div = num // 10
        num = (10**(length - 1) * rem) + div
        if is_prime(num): 
            circular_list.append(num)
     
    # if all circular variants are prime, their number is equal to length of number        
    if len(circular_list) == length:
        return(circular_list)
    
    else: return []



circular_primes = []
groups = []

# traverse all numbers lower than 1 million, we can traverse by 2, because even numberc cannot be prime
for i in range(3, 1000000, 2):
    if is_prime(i):
        circular_list = circulate(i)
        circular_primes = circular_primes + circular_list
        groups.append(circular_list)


# add 2 - the only even prime number
circular_primes.insert(0, 2)

# take only unique values
unique_circular_primes = list(numpy.unique(circular_primes))

# print the length of list of circular primes
print(len(unique_circular_primes))












