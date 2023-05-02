# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 21:05:25 2023

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=66

# %% initial code - not computationally optimal
import math

MAX = 1000
# define a function that checks if number is a square
def is_square(n):
    return int(math.sqrt(n))**2 == n

# generate all non-square numbers up to 1000
all_d = [x for x in range(MAX+1) if is_square(x) == False]

# for every D find a minimal x that meets the diophantine equation 
dictionary = {}
for d in all_d:
    x = 1
    while True:
        y = 1
        while y < x:
            if x**2 - d * y**2 == 1:
                
                dictionary[d] = [x, y]
                break
            y += 1
        if x**2 - d * y**2 == 1:
            break
        x += 1


current_max = 0
current_d = 0
# traverse through the dictionary and find the D for maximal X
for key, value in dictionary.items():
    if value[0] > current_max:
        current_max = value[0]
        current_d = key
        
print(current_d)



# %% -------------------------------------------------------
# https://radiusofcircle.blogspot.com/2017/01/project-euler-problem-66-solution-with-python.html


# square root function
from math import sqrt
n = 13

# function to calculate the continued fraction
def cf(n):
    mn = 0.0
    dn = 1.0
    a0 = int(sqrt(n))
    an = int(sqrt(n))
    convergents = [a0]
    period = 0
    if a0 != sqrt(n):
        while an != 2*a0:
            mn = dn*an - mn
            dn = (n - mn**2)/dn
            an = int((a0 + mn)/dn)
            convergents.append(an)
    return convergents[:-1]

x = cf(13)

def cf_inv(cf):
    """
    function to calculate the
    simple fraction from the continued
    fraction.
    """
    numerator = 1
    denominator = cf.pop()
    while cf:
        denominator, numerator = denominator*cf.pop() + numerator, denominator
    return denominator, numerator

cf_inv(x)


# variable to store the largest value 
# and the place it occurs
largest = 0, 0

# for loop less than 1000
for i in range(1, 1001):
    if i%sqrt(i) != 0:
        continued_fraction = cf(i)
        if len(continued_fraction) % 2 != 0:
            u, v = cf_inv(continued_fraction)
            u, v = 2*u**2+1, 2*u*v
        else:
            u, v = cf_inv(continued_fraction)
        if u > largest[1]:
            largest = i, u

# print the largest value
print(largest[0])