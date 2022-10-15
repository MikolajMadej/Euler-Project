# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 12:33:14 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=5


# manual solution
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20

# jeżeli 20, to 1, 2, 4, 5, 10 też
# jeżeli 19 to 19 dodatkowo
# jeżeli 18 to 9, 6, 3 dodatkowo
# jeżeli 17 to 17 dodatkowo
# jeżeli 16 to 8 dodatkowo
# jeżeli 14 to 7 dodatkowo
# jeżeli 13 to 13 dodatkowo
# jeżeli 11 to 11 dodatkowo

"""
20|19|18|17|16|14|13|11
"""

20*19*9 *17*4* 7*13*11
 


# import greatest common denominator function
from functools import reduce
from math import gcd                                                           

# implement lowest common multiple function
def lcm(a,b):
    "Calculate the lowest common multiple of two integers a and b"
    return a*b//gcd(a,b)                                                       # // to floor division, dzieli a*b przez gcd(a, b) i zaokrągla do dołu

# gcd(7, 12)
# lcm(7, 12)

# gcd(12, 16)
# lcm(12, 16)

# reduce(lcm, range(1,10+1))

# pritn output
reduce(lcm, range(1,20+1))
