# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 14:46:22 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=58


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



# initiate starting number and count of primes
count_of_primes = 0
current_number = 1


# while loop is the "level" of the spiral
i = 1
while True:
     
    
    # k loop is 4 sides of every level
    for k in range(1, 5, 1):
        
        # start from 1 , add 2, 2, 2, 2, 4, 4, 4, 4, 6, 6... ect
        current_number = current_number + (2 * i)
        
        # check if corner number is prime, if yes - add it to count
        if is_prime(current_number):
            count_of_primes += 1
            
        # calculate ratio of primes on diagonal
        ratio = count_of_primes / (1 + (4 * i))
        
        # print for visibility
        print(ratio)
        
        # check if ratio is lower than 0.1
        if ratio < 0.1:
            print(i * 2 + 1)
            break
    
    # break out of the outer loop as well
    if ratio < 0.1:
        break
    
    i += 1
