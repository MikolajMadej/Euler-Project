# -*- coding: utf-8 -*-
"""
Created on Fri Oct 21 22:11:00 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=33

numerator_lst = []
denominator_lst = []

for numerator in range(10, 100):
    for denominator in range(10, 100):
        num = list(map(int, list(str(numerator))))
        den = list(map(int, list(str(denominator))))
        
        if (num[1] == 0 or den[1] == 0):
            
            continue
        
        elif (num[0] == den[1]) and (numerator/denominator == num[1]/den[0]) and (numerator != denominator) and (numerator < denominator):
            
            numerator_lst.append(numerator)
            denominator_lst.append(denominator)
            
        elif (num[1] == den[0]) and (numerator/denominator == num[0]/den[1]) and (numerator != denominator) and (numerator < denominator):
            
                numerator_lst.append(numerator)
                denominator_lst.append(denominator) 

        else: continue                                         
                                                                                

import math

numerator   = math.prod(numerator_lst)
denominator = math.prod(denominator_lst)
print(int(1/(numerator/denominator)))
