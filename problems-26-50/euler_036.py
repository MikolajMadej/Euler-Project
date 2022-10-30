# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 12:41:32 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=36


# define a function that checks if number is a palindrome
def check_if_palindrome(number):
    
    # convert number to string and assume it is a palindrome
    number_str = str(number)
    output = True
    
    # if at least one mirror reflection pair of digits is different change assumption to false
    for i in range(0, len(number_str), 1):
        if number_str[i] != number_str[-(i+1)]:
            output = False
    return output


# initiate sum of palindromic numbers in bse-2
sum_of_palindromes = 0


# iterate through all numbers smaller than 1 m and if both are palindromic add base-2 to sum
for i in range(1, 1000000, 1):
    if check_if_palindrome(i) and check_if_palindrome(bin(i)[2:]):             # bin returns number in binary form, but as a string with '0b' in the beginning 
        sum_of_palindromes = sum_of_palindromes + i
    
    
    
# print sum of palindromic numbers
print(sum_of_palindromes)
