# -*- coding: utf-8 -*-
"""
Created on Sat Oct 29 14:54:12 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=40

# initiate i for while loop and an empty sting that will hold all the numbers 
i = 1
string = ""

# add 1, 2, 3, 4... to string
while True:
    string = string + str(i)
    if len(string) >= 1000000:
        break
    i += 1

# summarise all numbers that sit on 10 powers spots
sum_of_nums = 1
for i in [1, 10, 10**2, 10**3, 10**4, 10**5, 10**6]:
    sum_of_nums = sum_of_nums * int(string[i-1])   
    

# print their product
print(sum_of_nums)