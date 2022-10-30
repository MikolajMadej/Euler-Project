# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 13:48:08 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=50


import math

# define the upper bound
max_bound = 1000000


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


# create list of primes 
for i in range(1, max_bound + 1, 1):         
    if is_prime(i):
        list_of_primes.append(i)

del i

length = len(list_of_primes)


# initiate number of max consecutive primes which sum is a prime
max_hits = 0
max_prime = 0


bound_for_j = length


# below solution makes use of slices
# i - start point for slicing list of primes
# j - end point for slicing


# traversing from 0 to 78'497
for i in range(length):
    
    # traversing from 0 to 78'497
    # starting j will be updated every time we get a new max_hits number, to look only for thise that have a chance to be bigger 
    # bound for j will be updated (by 1 to follow the increment of i) if we exceed the sum 
    for j in range(i + max_hits, bound_for_j):
        current_sum = sum(list_of_primes[i:j])
        if current_sum < max_bound:
            if current_sum in list_of_primes:
                max_hits = j-i
                max_prime = current_sum
                
        else:
            bound_for_j = j + 1
            break 

print(max_hits)
print(max_prime)








#### below is extra slow
# for i in range(length):
    
#     hits = 1
#     current_sum = list_of_primes[i]
    
#     for j in range(1, length-i):
#         current_sum = current_sum + list_of_primes[j+i]
#         if current_sum > max_bound:
#             break
#         hits = j+1
        
#         if current_sum in list_of_primes and hits > max_hits:
#             max_hits = hits
#             max_prime = current_sum

# print(max_hits)
# print(max_prime)
