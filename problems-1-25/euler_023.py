# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 14:20:46 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=23


import numpy

# define a function that calculates a sum of proper divisors of a given number
def sum_of_proper_divisors(number):
    proper_divisors = []
    for i in range(1, int((number/2+1))):
        if number % i == 0:
            proper_divisors.append(i)
    return(sum(proper_divisors))


# all numbers greater than 28123 can be written as the sum of two abundant numbers, so the below code is constrained to 28123
# find all abundant numbers below 28124
abundant_numbers = []
for i in range(1, 28123+1):
    if sum_of_proper_divisors(i) > i:
        abundant_numbers.append(i)


# how many possible pairs there are
# int((len(abundant_numbers)*(len(abundant_numbers)-1))/2)

# define a function that traverses through abundant numbers list and connects them into pairs. Those pairs are summed. 
def two_number_combos(input_list):
    output_list = []
    for starting_number in range(len(input_list)):
        for second_number in range(1, len(input_list) - starting_number):
            sum_of_numbers = input_list[starting_number] + input_list[starting_number + second_number]
            output_list.append(sum_of_numbers)
    return list(numpy.unique(output_list))


# find all possible sums of two different abundant numbers
sums_of_pairs = two_number_combos(abundant_numbers)

# find all sums of two same abundant numbers
own_sum = []
for i in abundant_numbers:
    own_sum.append(i+i)
    
# bind both above defined lists
final_list = list(numpy.unique(sums_of_pairs + own_sum))

# filter out values above 28123
filtered = []
for pair in final_list:
    if pair <= 28123:
        filtered.append(pair)
        

# calculate difference between sum of all integers from 1 to 28123 and sum of all numbers that can be written as a sum of two abundant numbers
sum(range(1, 28123+1)) - sum(filtered)
