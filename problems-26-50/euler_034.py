# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 23:20:29 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=34


# find the lower and upper bound for traversing by implementing a factorial function and manual testing
def factorial(count):
    output = 1
    for i in range(1, count+1):
        output = output * i
    return(output)

# 1-digit number results in at max 6 digit number
# factorial(9)*1

# 9-digit number results in at max 7 digit number
# factorial(9)*9

lower_bound = 10
upper_bound = factorial(9) * 7


# define a function that transforms a number to a sum of factorials of its digits
def transform_to_factorial(number):
    
    factorial_sum = 0
    for i in range(len(str(number))):
        
        # The // performs floor division by a power of ten to move the digit to the ones position, 
        # then the % gets the remainder after division by 10. The numbering in this scheme 
        # uses zero-indexing and starts from the right side of the number.
        
        digit = factorial(number // 10**i % 10)
        factorial_sum = factorial_sum + digit
    return(factorial_sum)


# initiate a sum o numbers that are equal to sum of factorials of their digits
digit_factorial_sum = 0

# if number meets condition, add it to sum
for i in range(lower_bound, upper_bound+1):
    if i == transform_to_factorial(i):
        digit_factorial_sum = digit_factorial_sum + i
        
        
print(digit_factorial_sum)