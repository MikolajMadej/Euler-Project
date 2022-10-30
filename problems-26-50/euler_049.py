# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 12:22:33 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=49


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


# min is the first number from triplet given in problem description
min_bound = 1488

# max is the last number that can by added to 6660 and still by 4-digit
max_bound = 10000-3330-3330+1


# traverse all 4-digit numbers between min and max bounds
for i in range(min_bound, max_bound):
    
    # calculate all 3 numbers from the triplet
    num_1st = i
    num_2nd = i + 3330
    num_3rd = i + 3330 + 3330
    
    # transform them to lists of digits
    num_1st_lst = list(map(int, str(num_1st)))
    num_2nd_lst = list(map(int, str(num_2nd)))
    num_3rd_lst = list(map(int, str(num_3rd)))
    
    # sort the lists
    num_1st_lst.sort()
    num_2nd_lst.sort()
    num_3rd_lst.sort()
    
    # check if all 3 are primes and if sorted litst are identical (if yes, they are permutations)
    if is_prime(num_1st) & is_prime(num_2nd) & is_prime(num_3rd) & (num_1st_lst == num_2nd_lst == num_3rd_lst):
        print(str(num_1st) + str(num_2nd) + str(num_3rd))
        break