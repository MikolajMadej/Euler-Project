# -*- coding: utf-8 -*-
"""
Created on Sun Dec  4 21:12:36 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=60

import math

# define the upper bound
max_bound = 20000


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


# initiate list of primes
list_of_primes = []

# create list of 1 million primes (we are looking for the smallest, if the algorithm fails, we can broaden the search)
for i in range(1, max_bound + 1, 1):         
    if is_prime(i):
        list_of_primes.append(i)
        
list_of_primes[-10:]

#we can pop 2, because by concatenating it at the end we will always end up with an even (so not prime) number
list_of_primes.pop(0)

# define a function that combines two numbers and checks if both are prime
def combine(a, b):
    comb_1 = int(str(a) + str(b))
    comb_2 = int(str(b) + str(a))
    
    if is_prime(comb_1) and is_prime(comb_2):
        return True
    else: 
        return False
    


# main loop
# start with first prime on the list (a)
for id_a, a in enumerate(list_of_primes):
    
    # b is the next prime on the list
    for id_b, b in enumerate(list_of_primes[id_a:]):
        
        # check if combining a and b also gives only primes
        if combine(a, b):
            
            # iteratively add c, d,and a to our 5-length vector and check if adding further numbrs also concatenates to primes only
            for id_c, c in enumerate(list_of_primes[(id_a+id_b):]):
                if combine(a, c) and combine(b, c):
                    for id_d, d in enumerate(list_of_primes[(id_a+id_b+id_c):]):
                        if combine(a, d) and combine(b, d) and combine(c, d):
                            for id_e, e in enumerate(list_of_primes[(id_a+id_b+id_c+id_d):]):
                                if combine(a, e) and combine(b, e) and combine(c, e) and combine(d, e):
                                    print(a, b, c, d, e, a+b+c+d+e)
