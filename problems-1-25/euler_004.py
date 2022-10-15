# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 10:16:07 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=4


output_list = []
divider_list = []

# check all numbers which are products of multipliaction of 2 3-digit numbers
for number in range(999*999, 100*100, -1):
    
    # look for palindromes
    number_text = str(number)
    if number_text[0] == number_text[-1] and number_text[1] == number_text[-2] and number_text[2] == number_text[-3]:
        
        # assume palindrome doesn't have 3-digit divider
        output_list.append(number)
        divider_list.append("no 3-digit divider")

        # check if palindrome can be written as a product of 2 3-digit numbers
        for divider in range (999, 100, -1): 
            if not(number % divider == 0 and len(str(divider)) == 3 and len(str(int(number / divider))) == 3):
                continue

            else:
                
                # if they can, replace "no 3-digit divider" with existing divider
                divider_list.pop()
                divider_list.append(divider)
                break
            

# list comprehension
# indices = [i for i, x in enumerate(divider_list) if x == "no 3-digit divider"]


# filter out all palindromes without 3-digit dividers
for index in range(len(divider_list)):
    if divider_list[index] == "no 3-digit divider":
        divider_list[index] = "out"
        output_list[index]  = "out"
        
        
divider_list = list(filter(("out").__ne__, divider_list))    # __ne__ is not equal
output_list =  list(filter(("out").__ne__, output_list))


# list comprehension
# divider_list = [ i for i in divider_list if i!="out" ]
# output_list  = [ i for i in output_list  if i!="out" ]

# print max palindrome
max(output_list)
