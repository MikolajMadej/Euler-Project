# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 17:58:38 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=43


# import the permutations method and create all pandigitals
from itertools import permutations
all_pandigitals = list(permutations('0123456789'))

# initiate sum of all panidigitals that meet all 7 conditions
sum_of_pandigitals = 0 


for current_pandigital in all_pandigitals:
    
    # transform tuple to string
    current_number = ""
    for i in range(len(current_pandigital)):
        current_number = current_number + current_pandigital[i] 
   
    # check all 7 conditions at once
    if int(current_number[1:4])  % 2  == 0 and \
       int(current_number[2:5])  % 3  == 0 and \
       int(current_number[3:6])  % 5  == 0 and \
       int(current_number[4:7])  % 7  == 0 and \
       int(current_number[5:8])  % 11 == 0 and \
       int(current_number[6:9])  % 13 == 0 and \
       int(current_number[7:10]) % 17 == 0:
           
        sum_of_pandigitals = sum_of_pandigitals + int(current_number)
        

# print the sum
print(sum_of_pandigitals)
