# -*- coding: utf-8 -*-
"""
Created on Sun Feb 19 15:13:08 2023

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=99

import requests
from math import log

# get the data and transformt o list
data = requests.get('https://projecteuler.net/project/resources/p099_base_exp.txt').text 
lst_data = data.split("\n")
lst_final = [x.split(",") for x in lst_data]

# initiate variables storing max values
max_value = 0
max_row   = 0

# try every row, log(x^y) = y*log(x), so by comparing y*log(x) instead of x^y we avoid working with extra large numbers
for i, values in enumerate(lst_final):
    value = int(values[1])*log(int(values[0]))
    
    if value > max_value:
        max_value = value
        max_row = i + 1


# print result    
print(max_row, max_value)