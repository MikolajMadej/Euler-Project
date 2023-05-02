# -*- coding: utf-8 -*-
"""
Created on Sun Apr  2 19:32:17 2023

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=80


# %pip install sympy

import math
import sympy as sympy


output = 0
my_dict = {}

for i in range(101):
    if math.sqrt(i) == int(math.sqrt(i)):
        continue
    
    num = sympy.N(sympy.sqrt(i), 110)
    fin = str(num).replace(".", "")[:100]
    final_sum = sum(int(x) for x in fin)
        
    print("My solution: ", final_sum)
    my_dict[i] = final_sum
    output += final_sum
    
print(output)

# 40886


# %% solution without external packages, https://www.educative.io/answers/how-to-solve-project-euler-80
# dSum calculates digital sum of n
def dSum(n):
    sum = 0
    while n!=0:
        sum+=n%10
        n//=10
    return sum

# fastRoot will calculate root of n with 100 decimal digit precision.

n = 2
def fastRoot(n):
    a=5*n
    b=5
    limit = 10**(101)
    while b<limit:
        if a>=b:
            a-=b
            b+=10
        else:
            a*=100 
            b= (b-b%10)*10 + b%10

    root = int(str(b)[:100])
    return root

result=0
good_dict = {}
for n in range(1,101):
    if n not in [1,4,9,16,25,36,49,64,81,100]:
        rootN = fastRoot(n)
        print(dSum(rootN))
        good_dict[n] = dSum(rootN)
        result += dSum(rootN)


print(result)

