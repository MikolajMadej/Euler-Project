# -*- coding: utf-8 -*-
"""
Created on Sun Oct  2 21:22:22 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=12


# formula for number of divisors:
# (a+1)*(b+1)*(c+1)... where a, b, c are counts of consecutive prime factors

# What is the value of the first triangle number to have over five hundred divisors?
how_many_divisors = 500
   
# Define a function that finds prime factors of a number
def find_prime_factors(number):
    prime_list = []
    i = 2
    while number > 1:
        if number % i == 0:
            number = number / i
            prime_list.append(i)
            i = 2
        else: i += 1
    return(prime_list)   
        
# count appearances of same prime factors, eg. 2, 2, 2, 3, 3, 7 -> 3, 2, 1
def count_same_prime_factors(input_list):
    output_list = [1]
    for i in range(1, len(input_list)):
        if input_list[i] == input_list[i-1]:
            output_list[-1] = output_list[-1] + 1
        else: output_list.append(1)
    return(output_list)


# multiply all numbers in a list
def multiply_all(input_list):
    output = 1
    for i in range(len(input_list)):
        output = output * input_list[i]
    return(output)

# add one to every number on a list
def add_one(input_list):
    output_list = [0] * len(input_list)
    for i in range(len(input_list)):
        output_list[i] = input_list[i] + 1
    return(output_list)
        

    
# break the loop when first number with over 500 divisors is found
triangle_number = 1
i = 1
while True:
    prime_factors = find_prime_factors(triangle_number)
    count_of_factors = count_same_prime_factors(prime_factors)
    adjusted_factors = add_one(count_of_factors)
    number_of_factors = multiply_all(adjusted_factors)
    if number_of_factors > how_many_divisors:                         
        print(triangle_number)
        break
    
    # iterate for every triangle number (1, 1+2 = 3, 1+2+3 = 6, ect.)
    i += 1
    triangle_number = triangle_number + i
    