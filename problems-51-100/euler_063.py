# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 18:16:34 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=63

# initiate the count
count = 0

# brute force check all possible outcomes, assuming max power 100 and number 100000
# start from 1 because we are looking only for positive integers
for power in range(1, 100):
    for number in range(1, 100000):
        output = number**power
        length = len(str(output))
        
        if power == length:
            print(number, "^", power, "=", output)
            count +=1

# print the output
print(count)
