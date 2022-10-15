# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 13:00:00 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=24


# def factorial(count):
#     output = 1
#     for i in range(1, count+1):
#         output = output * i
#     return(output)

# factorial(9)

# 362'880 first permutations start with 0
# 362'880 further permutations start with 1
# the permutation we are loocking for starts with 2
# to be more precise we are looking for  274'240th permutation starting with 2

# factorial(8)

# 40'320 first permutations starting with 2, in fact start with 20
# 40'320 further permutations start with 21
# 40'320 further permutations start with 23
# 40'320 further permutations start with 24 (112'960 left)
# 40'320 further permutations start with 25 ( 72'640 left)
# 40'320 further permutations start with 26 ( 32'320 left)
# the permutation we are looking for starts with 27

# factorial(7)

# 5'040 first permutations starting with 27, in fact start with 270 (27'280 left)
# 5'040 further permutations start with 271 (22'240 left)
# 5'040 further permutations start with 273 (17'200 left)
# 5'040 further permutations start with 274 (12'160 left)
# 5'040 further permutations start with 275 ( 7'120 left)
# 5'040 further permutations start with 276 ( 2'080 left)

# we are looking for 2'080 permutation starting with 278. Numbers available are [0, 1, 3, 4, 5, 6, 9]



# define list of available digits
digits = ['0', "1", "2", "3", "4", "5", "6", "7", "8", "9"]

# define output list
result = []

# define how many permutations prior to our desired one we have
how_many_left = 999999 

# define function that calculates a factorial for a given number
def factorial(count):
    output = 1
    for i in range(1, count+1):
        output = output * i
    return(output)


for i in range(len(digits) - 1, -1, -1):                                       # traversing from 9 to 0 (both inclusive)
    rest = divmod(how_many_left, factorial(i))[1]                              # get rest from division
    number = divmod(how_many_left, factorial(i))[0]                            # get number of full divisions
    result.append(digits[number])                                              # append consecutive digits of output number*

    digits.pop(number)                                                         # pop number from list of available digits

    how_many_left = rest


# define empty string and join it with our output list. Display it as integer. 
string = ""
print(int(string.join(result)))



# *consecutive numbers of output number are defined as follows:
# factorial(9) = 362'880, so all permutations starting with 0 and with 1 are priot to 1-mil permutation
# 362'880 fits in 1mil over two times - our desired number starts with 3rd digit (0, 1, 2, 3,...) so with 2
# we can append 2 as the first digit in our output number