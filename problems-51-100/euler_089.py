# -*- coding: utf-8 -*-
"""
Created on Sat Apr 22 15:50:18 2023

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=91

import requests
data = requests.get("https://projecteuler.net/project/resources/p089_roman.txt").text

data = data.split("\n")

start_len = sum(len(word) for word in data)

def optimise(number):
    result = number
    
    replacements = [
    ("VIIII", "IX"), 
    ("IIII", "IV"), 
    ("LXXXX", "XC"), 
    ("XXXX", "XL"),
    ("DCCCC", "CM"), 
    ("CCCC", "CD")]
    
    for old, new in replacements:
        result = result.replace(old, new)
        
    return result
    
optimised_len = 0

for word in data:
    optimised = optimise(word)
    optimised_len += len(optimised)
    
    
print(start_len - optimised_len)