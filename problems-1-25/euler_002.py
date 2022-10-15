# -*- coding: utf-8 -*-
"""
Created on Thu Sep 29 22:08:39 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=2


# declare fibinacci list
fibonacci_list = [1]

# calculate all fibonacci numbers below 4-mil
i = 2
while i < 4000000:
    fibonacci_list.append(i)
    i = fibonacci_list[-1] + fibonacci_list[-2]

# create a list of even valued fiboancci numbers below 4-mil
fibonacci_list_copy = []
for fib in fibonacci_list:
    if fib % 2 == 1:
        fibonacci_list_copy.append(0)
    else:
        fibonacci_list_copy.append(fib)
            

# print the sum
sum(fibonacci_list_copy)





## Alternative solution without creating list duplicate
fibonacci_list = [1]
i = 2
while i < 4000000:
    fibonacci_list.append(i)
    i = fibonacci_list[-1] + fibonacci_list[-2]
    
for fib in range(len(fibonacci_list)):
    if fibonacci_list[fib] % 2 == 1:
        fibonacci_list[fib] = 0
            

sum(fibonacci_list)