# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 15:12:15 2023

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=87

# 50'000'000 = a**2 + b**3 + c**4
import math
MAX = 5 * 10**7
max_num = int(math.sqrt(MAX - 2**3 - 2**4))

# generate primes using erastothenes sieve
def generatePrimes(limit):
    limitn = limit+1
    not_prime = set()
    primes = []

    for i in range(2, limitn):
        if i in not_prime:
            continue

        for f in range(i*2, limitn, i):
            not_prime.add(f)

        primes.append(i)

    return primes

primes = generatePrimes(max_num)


sum_list = set()
count = 0
for a in primes:
    if a**4 > MAX:
        break
    for b in primes:
        if b**3 + a**4 > MAX:
            break
        for c in primes:
            output = c**2 + b**3 + a**4
            if output < MAX and output not in sum_list:
                count += 1
                sum_list.add(output)
                
print(count)
