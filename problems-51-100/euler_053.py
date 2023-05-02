# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 19:14:23 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=53

# define a funstion that calcuates the factorial for number x
def factorial(count):
    output = 1
    for i in range(1, count+1):
        output = output * i
    return(output)

# factorail of 10 is the first factorial greater than 1 million
factorial(10)

# initiate list of factorials
list_of_factorials = []

# calculate all the newton signs according to formula from problem description
for n in range(10, 101, 1):
    for r in range(1, n):
        num = int(factorial(n) / (factorial(r) * factorial(n - r)))
        if num > 1000000:
            list_of_factorials.append(num)


# print result
print(len(list_of_factorials))
