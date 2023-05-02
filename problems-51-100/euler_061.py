# -*- coding: utf-8 -*-
"""
Created on Sun Jan 22 19:22:04 2023

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=61

# set min and max for numbers generators (only 4 digit numbers)
min_range = 1000
max_range = 9999 


# create list of generators using lambda statement
lst_lambda = [    
    lambda x: x*(x+1)//2,
    lambda x: x**2,
    lambda x: x*(3*x-1)//2,         # // zamiast / - dzielenie całkowite
    lambda x: x*(2*x-1), 
    lambda x: x*(5*x-3)//2,
    lambda x: x*(3*x-2)          
    ]
    

# initiate the list of list of numbers
lst_total = []

# fill main list with sublists
for current_lambda in lst_lambda:
    
    i = 0
    partial = []
    while current_lambda(i) <= max_range:
        if current_lambda(i) >= min_range:
            partial.append(current_lambda(i))
        i += 1
        
    lst_total.append(partial)  

# clear the environment
list(map(len, lst_total))
del lst_lambda, i, max_range, min_range, partial


# recursion
def check_from_start_point(used_numbers, used_types):
    
    # check if the numbers "loop", that is if the last 2 digits of the last numbers are 2 first digits of first number
    if len(used_types) == 6 and used_numbers[0] // 100 == used_numbers[-1] % 100:
        print(used_numbers, used_types, sum(used_numbers))
        
    else:
        for t in range(0, 6):
           if t not in used_types:
              
               for n in range(len(lst_total[t])):
                       if used_numbers[-1] % 100 == lst_total[t][n] // 100: 
                           
                           new_used_numbers = list(used_numbers)                          # overwrite the list to clear it before recursive pass-on
                           new_used_types = list(used_types)
                           
                           new_used_numbers.append(lst_total[t][n])
                           new_used_types.append(t)
                           
                           # recursion
                           check_from_start_point(new_used_numbers, new_used_types)
                       
                       
                              

# lets start with every triangle number
for number in lst_total[0]:
    check_from_start_point([number], [0])
    

