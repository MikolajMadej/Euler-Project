# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 14:01:52 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=17

# number of letters in words
# one 3
# two 3
# three 5
# four 4
# five 4
# six 3
# seven 5
# eight 5
# nine 4
# ten 3
# eleven 6
# twelve 6
# thir teen 4+4
# four teen
# five teen
# six teen
# seven teen
# eigh teen
# nine teen
# twen ty 6
# thir ty 6
# for ty 5
# fif ty 5
# six ty 5
# seven ty 7
# eigh ty 6
# nine ty 6
# one hundred 10
# one thousand 11
# hundred and 10

# Numbers 1-9

a = 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4

# Numbers 10-19

b = 3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8 

# Numbers 20-99

c = 8 * a + 10 * (6 + 6 + 5 + 5 + 5 + 7 + 6 + 6)

# Numbers 100-999

d1 = 36*100
d2 = 9*854
d3 = 7*9 
d4 = 9*99*10

# 1000

e = 11


final = a + b + c + d1 + d2 + d3 + d4 +  e
print(final)
