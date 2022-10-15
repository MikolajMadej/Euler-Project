# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 21:51:20 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=14


max_link_length = 1
current_winner = 1

# check every number below 1 million
for starting_point in range(2, 1000000, 1):
    
    current_count = 1
    chain_link = starting_point
    
    # if number is odd multiply by 2 and add 1 if is even, divide by 2. Break when number reaches one
    while chain_link > 1:
        link_length = current_count
        if chain_link % 2 == 0:
            chain_link = int(chain_link/2)
            current_count += 1                          # calculate chain length
        else: 
            chain_link = int(chain_link*3+1)
            current_count += 1
    
    # overwirite if current length is the biggest
    if current_count > max_link_length:
        current_winner = starting_point
        
    max_link_length = max(current_count, max_link_length)
    

print(current_winner, max_link_length)