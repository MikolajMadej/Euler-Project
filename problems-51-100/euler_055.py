# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 14:19:04 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=55

# define a function that checks if string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

# initiate number of non-Lychrel numbers
number_of_not_lychrel = 0


# check all numbers 1-10000
for i in range(1, 10001, 1):
        
    # if after 50 iterations there is no palindrome, the number is a lyrchel number
    for j in range(1, 51, 1):
        
        i_as_string = str(i)
        reverse = i_as_string[::-1]
        i = int(i_as_string) + int(reverse)
        
        if is_palindrome(str(i)):
            number_of_not_lychrel += 1
            break


# print number of lyrchel numbers
print(10000 - number_of_not_lychrel)
