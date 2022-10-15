# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 15:27:18 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=20


# define a funstion that calcuates the factorial for number x
def factorial(count):
    output = 1
    for i in range(1, count+1):
        output = output * i
    return(output)


# calculate factorial of 100
output = factorial(100)


# calculate sum of digits in this number
sum(list(map(int, str(output))))