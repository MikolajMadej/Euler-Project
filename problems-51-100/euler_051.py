# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 13:42:21 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=51

# First prime in the eight prime family is 121313
# we need to have an 8-member family, and are looking for the smalles number of the family, so its "replaceable"
# number(s) will be 0, 1 or 2
# eg. 3006087 or 3116187 or 3226287, because by replacing with 3-9 we get 7 remaining  family members 

# cyfra, która sięw naszej liczbie powtarza (i ktorą bedziemy zamieniac) musi występować dokładnie 3 razy
# 7727 -> 1121, 2222, 3323, 4424, 5525, 6626, 8828, 9929 -> żadna nie jest podzielna przez 3, każda jest potencjalnie pierwsza 
# 7741 -> 1141, 2241, 3341, 4441, 5541, 6641, 8841, 9941 -> 2241, 5541, 8841 są podzielne przez 3, nigdy nie uzyskamy 8 liczb pierwszych
# tak samo bedzie jak bedziemy zamieniac 1, 4, 5 cyfr...

# ostatniej cyfry nie mozemy zamieniac, bo dla n > 10 tylko liczby konczace sie na 1, 3, 7, 9 moga byc pierwsze, czyli
# nie uzyskalibysmy 8 roznych

import math

# define the upper bound
max_bound = 1000000


# define a function that returns True if a number is prime
def is_prime(num):
    
    # edge condition - 2 is prime
    if num == 2:
        return True
    
    # numbers below 2 (esp. negative ones) are not prime
    elif num < 2:
        return False
    
    for div in range(2, math.ceil(math.sqrt(num))+1):
        if num % div == 0:
            return False
        
    return True


# initiate list of primes
list_of_primes = []


# create list of 1 million primes (we are looking for the smallest, if the algorithm fails, we can broaden the search)
for i in range(1, max_bound + 1, 1):         
    if is_prime(i):
        list_of_primes.append(i)
 

# filter our ilst of primes (number needs to have 3*"0" or 3*"1" or 3*"2")
# filter(fn, list)
filtered_primes = list(filter(lambda min_val: min_val >= 10, list_of_primes))       # filter is used same way as map()

# take only primes that have at least 3 duplicated digits
final_primes = [x for x in filtered_primes if len(str(x)) - len(set(str(x))) >= 3]


# define a function that counts digits in a number
def count_digits(number, digit):
    num = str(number)
    count = num.count(str(digit))
    return(count)

# initate a list to append only primes that have 3*"0" or 3*"1" or 3*"2"
selected_primes = []

# take only primes that have 3*"0" or 3*"1" or 3*"2"
for prime in final_primes:
    if count_digits(prime, 0) == 3 or  count_digits(prime, 1) == 3 or count_digits(prime, 2) == 3:
        selected_primes.append(prime)
        
# we are sure that on our list there are no such 6-digit numbers that have only two different dgits
# these numbers would be divisible by 3


# for all remaining primes, replace all three duplicated numbers with all other possibilities and 
# check how many prime numbers we get in this action
# if 8 - this is the number we are looking for

for number in selected_primes:
    if count_digits(number, 0) == 3:
        number_str = str(number)
        others = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
        count = 1
        for other in others:
            number_rep = number_str.replace("0", other)
            if int(number_rep) in final_primes:
                count += 1
        
        if count == 8:
            print(number)
            break

    if count_digits(number, 1) == 3:
        number_str = str(number)
        others = ["0", "2", "3", "4", "5", "6", "7", "8", "9"]
        count = 1
        for other in others:
            number_rep = number_str.replace("1", other)
            if int(number_rep) in final_primes:
                count += 1
        
        if count == 8:
            print(number)
            break
        
    if count_digits(number, 2) == 3:
        number_str = str(number)
        others = ["0", "1", "3", "4", "5", "6", "7", "8", "9"]
        count = 1
        for other in others:
            number_rep = number_str.replace("2", other)
            if int(number_rep) in final_primes:
                count += 1
         
        if count == 8:
            print(number)
            break