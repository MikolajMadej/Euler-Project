# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 16:32:46 2023

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=75

# %% not optimal solution
MAX = 5000
how_many = 0

for i in range(MAX):
    current = 0
    current_set = set()
    for a in range(1, int(i/2)):
        for b in range(1, int(i)-a):
            c = (a**2 + b**2)**(1/2)
            if a + b + c == i and {a, b, c} != current_set:
                current_set = {a, b, c}
                current += 1
                # print(i, a, b, c)
    
    if current == 1:
        how_many +=1
        
        
        
# %% OPTIMAL SOLUTION USING EUCLID FORMULA
# Euclid’s formula says that, (a,b,c) are a Pythagorean triple when
# a = 2mn,  b = m^2-n^2, c = m^2+n^2
# where m > n, and (n+m) mod 2 == 1, and gcd(m, n) = 1

import math 

# set max length of wire
MAX = 1500000

# define the greatest common denominator function
def gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a    

# initiate triples
triples = set()

# generate all base euler tripples starting from 3
for m in range(1, int(math.sqrt(MAX))+1):
    for n in range(m-1, 0, -1):
        if  gcd(m, n) == 1 and (n+m) % 2 == 1:
            
            a = 2 * m * n
            b = m**2 - n**2
            c = m**2 + n**2
            
            if a + b + c <= MAX:
                triples.add((a, b, c))

# add all not base triples by multiplying base ones
triples_list = list(triples.copy())
triples_fin = triples_list.copy()

for triple in triples_list:
    sum_of_sides = sum(triple)
    how_many = int(MAX / sum_of_sides)
    for i in range(2, how_many + 1):
        triples_fin.append(tuple(elem * i for elem in triple))
    
# create a dictionary that holds information how many triples have a given sum-length of sides
dict_fin = {}
for triple in triples_fin:
    sum_of_sides = sum(triple)
    
    if sum_of_sides not in dict_fin:
        dict_fin[sum_of_sides] = 1
    
    else: dict_fin[sum_of_sides] += 1
 
# count those lengths that have exactly one triple       
count = 0
for i in dict_fin.values():
    if i == 1:
        count += 1
        
# print the result
print(count)
