# -*- coding: utf-8 -*-
"""
Created on Sun Oct 30 11:37:20 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=47


# Define a function that finds prime factors of a number
def find_prime_factors(number):
    prime_list = []
    i = 2
    while number > 1:
        if number % i == 0:
            number = number / i
            if i not in prime_list:
                prime_list.append(i)
        else: i += 1
    return(len(prime_list))


how_many = 4

# initiate start for loop - 2*3*5*7 is the smallest prime with 4 factors
i = 2*3*5*7
while True:
    
    assumption = True
    # if number has 4 distinct primes, check next 3 numbers if they also have 4 distinct primes
    if find_prime_factors(i) == how_many:
        for j in range(i, i+how_many, 1):
            if find_prime_factors(j) != how_many:
               assumption = False
    else:
        assumption = False
        
    if assumption:
        print(i)
        break
    i += 1
    
    
    
    
    
# Faster version (npf algo taken from https://radiusofcircle.blogspot.com/2016/06/problem-47-project-euler-solution-with-python.html)
def npf(number):
    """function which will return
    the number of prime factors"""
    i = 2
    a = set()
    while i < number**0.5 or number == 1:
        if number % i == 0:
            number = number/i
            a.add(i)
            i -= 1
        i += 1
    return (len(a)+1)


how_many = 4

# initiate start for loop - 2*3*5*7 is the smallest prime with 4 factors
i = 2*3*5*7
while True:
    
    assumption = True
    if npf(i) == how_many:
        for j in range(i, i+how_many, 1):
            if npf(j) != how_many:
               assumption = False
    else:
        assumption = False
        
    if assumption:
        print(i)
        break
    i += 1
    
    

134043