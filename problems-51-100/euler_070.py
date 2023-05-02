# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 11:14:26 2023

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=70

MAX = 10000000

# my code adjusted from problem 69 
import math
from operator import mul
from functools import reduce

def factorize(n):
    res = []
    # iterate over all even numbers first.
    while n % 2 == 0:
        res.append(2)
        n //= 2
        # n = n // 2
        
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

minimum = MAX
n = 0


for i in range(2, MAX):
    num_lst = sorted([x for x in str(i)])
    totient_lst = sorted([x for x in str(int(totient(i)))])
    
    if num_lst == totient_lst:
        current = i / int(totient(i))
        
        if  current < minimum:
            minimum = current
            n = i
            
print(n)





# OPTIMISED BY ChatGPT-4

MAX = 10000000

def sieve(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i*i, limit + 1, i):
                primes[j] = False
    return [i for i in range(2, limit + 1) if primes[i]]

def factorize(n, primes):
    res = []
    for p in primes:
        if p*p > n:
            break
        while n % p == 0:
            res.append(p)
            n //= p
    if n > 1:
        res.append(n)
    return res

def totient(n, primes):
    factors = factorize(n, primes)
    tot = n
    for p in set(factors):
        tot *= (p-1)
        tot //= p
    return tot

primes = sieve(MAX)
minimum = MAX
n = 0

for i in range(2, MAX):
    totient_i = totient(i, primes)
    if sorted(str(i)) == sorted(str(totient_i)):
        current = i / totient_i
        if current < minimum:
            minimum = current
            n = i

print(n)




# further optimised by Chat-GPT 4
MAX = 10000000

from math import gcd, sqrt
from functools import reduce

def sieve_primes(limit):
    primes = [True] * (limit + 1)
    primes[0] = primes[1] = False
    for i in range(2, int(limit**0.5) + 1):
        if primes[i]:
            for j in range(i*i, limit + 1, i):
                primes[j] = False
    return [i for i in range(2, limit + 1) if primes[i]]

def square_free(limit):
    primes = sieve_primes(int(sqrt(limit)))
    factors = [[] for _ in range(limit+1)]
    for p in primes:
        for i in range(p*p, limit+1, p*p):
            factors[i].append(p*p)
    return [i for i in range(2, limit+1) if all(p not in factors[i] for p in factors[i-1])]

def factorize(n, primes):
    res = []
    for p in primes:
        if p*p > n:
            break
        while n % p == 0:
            res.append(p)
            n //= p
    if n > 1:
        res.append(n)
    return res

def totient(n, primes):
    factors = factorize(n, primes)
    tot = n
    for p in set(factors):
        tot *= (p-1)
        tot //= p
    return tot

square_free_numbers = square_free(MAX)
primes = sieve_primes(MAX)

minimum = MAX
n = 0

for i in square_free_numbers:
    totient_i = totient(i, primes)
    if sorted(str(i)) == sorted(str(totient_i)):
        current = i / totient_i
        if current < minimum:
            minimum = current
            n = i

print(n)




