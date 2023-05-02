# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 21:37:02 2023

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=69

# relatively prime numbers are numbers which greatest common denominator is equal to 1
# specify upper bound
MAX_BOUND = 1000000
    
# define function that looks for greatest common denominator
def greates_common_divisor(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x

# initialize placeholders for solution
max_count = 0
max_num = 0
max_totient = 0

# odd numbers will have low totients because they are relatively prime with more numbers
# we can skip them

for i in range(2, MAX_BOUND, 2):
    count = 0
    for j in range(1, i):
        if greates_common_divisor(i, j) == 1:
            count += 1
    
    totient = i / count
    if totient > max_totient:
        max_count = count
        max_num = i
        max_totient = totient
    
print(max_num, max_count, max_totient)

# NOTE: my code (above) is working well but is extremely inefficient
# below adjusted code from https://zach.se/project-euler-solutions/69/


import math
from operator import mul
from functools import reduce

def factorize(n):
    res = []
    # iterate over all even numbers first.
    while n % 2 == 0:
        res.append(2)
        n //= 2
    # try odd numbers up to sqrt(n)
    limit = math.sqrt(n+1)
    i = 3
    while i <= limit:
        if n % i == 0:
            res.append(i)
            n //= i
            limit = math.sqrt(n+i)
        else:
            i += 2
    if n != 1:
        res.append(n)
    return res


def totient(n):
    return n * reduce(mul, [1 - (1.0 / p) for p in set(factorize(n))])

# create list of tuples with 
fin_lst = [(n / totient(n), n) for n in range(2, 1000001)]   

#    
print(max(fin_lst))




# # initializing list
# test_list = [(2, 3), (4, 7), (8, 0), (3, 6)]
 
# # printing original list
# print ("The original list is : " + str(test_list))
 
# # using min() and max()
# # to get min and max in list of tuples
# res1 = min(test_list)[0], max(test_list)[0]
# res2 = min(test_list)[1], max(test_list)[1]
 
# # printing result
# print ("The min and max of index 1 : " + str(res1))
# print ("The min and max of index 2 : " + str(res2))

# %% itemgetter
# from operator import itemgetter
# max(fin_lst, key = itemgetter(0))
# max(fin_lst, key = itemgetter(1))

# min(fin_lst, key = itemgetter(0))
# min(fin_lst, key = itemgetter(1))
