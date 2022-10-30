# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 11:06:53 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=46

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

# check only number slower than 100000 (we are looking for the smalles such number, if needed this constant can be increased)
top = 100000


# lets start with making a list of primes lower than 1m
list_of_primes = []

for i in range(2, top+1):
    if is_prime(i):
        list_of_primes.append(i)
        
list_of_primes.pop(0)


# lets follow with making a list of composite odd numbers
list_of_composite_odds = []

for i in range(9, top+1, 2):
    if not is_prime(i):
        list_of_composite_odds.append(i)
        


# for every odd composite number try subtracting every lower prime number
for i in range(len(list_of_composite_odds)):
    
    current_odd = list_of_composite_odds[i]
    assumption = False
    
    j = 0
    while  list_of_primes[j] < current_odd:
        
        current_prime = list_of_primes[j]
        diff = int((current_odd - current_prime)/2)
        
        # if half of their difference is a perfect square, this number is complying with goldbach other conjecture
        if math.ceil(math.sqrt(diff)) == math.floor(math.sqrt(diff)):
            assumption = True
            break
        j += 1
    
    # if subtracting all primes didn't do it, this number cannot be expressed by goldbach equation
    # break the loop, we are looking for the forst one that doesn't meet these requrements
    if assumption == False:
        print(list_of_composite_odds[i])
        break
        
      
        