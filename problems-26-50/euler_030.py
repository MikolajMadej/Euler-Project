# -*- coding: utf-8 -*-
"""
Created on Sun Oct 16 13:39:59 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=30

# MAX len of numbers that can be written as sum of fifth powers of their nubers is 5
# 1 == len(str(1*9**5))
# 2 == len(str(2*9**5))
# 3 == len(str(3*9**5))
# 4 == len(str(4*9**5))
# 5 == len(str(5*9**5))
6 == len(str(6*9**5))
# 7 == len(str(7*9**5))
# 8 == len(str(8*9**5))
# 9 == len(str(9*9**5))


# define function that raises every number on the list to fifth power
def fifth_power(input_list):
    for i in range(len(input_list)):
        input_list[i] = input_list[i]**5
        


fitting_numbers = []

# check numbers from 10 to 999'999
for i in range(10, 1000000):
    i_list = list(map(int, str(i)))
    fifth_power(i_list)
    if sum(i_list) == i:
        fitting_numbers.append(i)
        
        
# print sum of numbers that meet this condition
sum(fitting_numbers)
