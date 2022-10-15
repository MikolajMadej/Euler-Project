# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 22:49:24 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=3


# define number for which largest prime will be found
number = 600851475143 

# starting from 1, divide our number by every divisor, until full orime factorisation is achieved
prime_list = []
for i in range(1, number):
    if number == 1:
        break
    if number % i == 0:
        number = number / i                                                    # update the number by dividing it by most recent prime factor
        prime_list.append(i)                                                   # append prime factor to the list
       
max(prime_list)


# WARNING: this solution works only for numbers for which prime factorisation consists of unique numbers
# (eg. does not work for 64, because prime factorisation for 64 consists of multiple 2s)
# robust function to find full prime factorisation available in solution to problem 12