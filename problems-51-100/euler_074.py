# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 12:54:46 2023

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=74

# initiate counter and problem conditions
count = 0
max_bound = 1000000
chain_lenght = 60

# define function that calculates factorial of a number
def factorial(count):
    output = 1
    for i in range(1, count + 1):
        output = output * i
    return(output)


# check all starting points
for i in range(1, max_bound):
   
    # save chain elements in a list
    current_list = [i]
    chain = i

    # continue the chain until it repeats
    while True:
        
        # transform number to its successor by calculating a sum of it's factorised digits
        digits = list(map(int, list(str(chain))))
        factorial_lst = list(map(lambda x:factorial(x), digits))
        chain = sum(factorial_lst)
        
        # append new unique chain vale in a list
        if chain not in current_list:
            current_list.append(chain)
        else:
            break
    
    # check if chain length is equal to problem condition
    if len(current_list) == chain_lenght:
        count += 1
        
        
# print answer        
print(count)
