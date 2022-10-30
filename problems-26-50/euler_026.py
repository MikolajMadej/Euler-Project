# -*- coding: utf-8 -*-
"""
Created on Sat Oct 15 15:59:17 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=26


# define a function that loks for recurring cycles in decimal representation of unit fractions
def length_of_recurring(number, denominator):
    
    # initiate lists for decimal digits, reminders after each division
    decimal = []
    reminder_bucket = []
    
    # multiply number by 10 to get first reminder (we always multiply 1 by a number greater than 1)
    reminder = (number * 10) % denominator
    
    # get first decimal number
    current_decimal = (number * 10) // denominator
    
    # loop until reminder is equal to 0 (division ends with no reminder)
    while (reminder != 0):
        
        decimal.append(current_decimal)
        reminder = reminder * 10
        
        # break if reminder duplicates (which means new cycle of recurring sequence starts)
        if reminder in reminder_bucket: 
            decimal.pop(-1)                                                    # pop last decimal if reminder duplicates
            break
        
        # append reminder, get current decimal and update reminder
        reminder_bucket.append(reminder)
        current_decimal = reminder//denominator
        reminder = reminder - denominator * current_decimal
    
    # append current decimal, get index of its first occurance 
    decimal.append(current_decimal)
    start_position = decimal.index(current_decimal)
    
    # get a subsequence from decimal list that starts with first occurence of starting digit 
    length = len(decimal[(start_position + 1):])
    
    return(length)


# check recurring cycles for every number from 1 to 999
max_len = 0
number_max = 0
for i in range(1, 1000):
    current_len = length_of_recurring(1, i)
    
    if current_len > max_len:
        max_len = current_len
        number_max = i


# print number for which cycle is the longest
print(number_max)


