# -*- coding: utf-8 -*-
"""
Created on Fri Apr  7 16:13:12 2023

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=77


MAX = 100

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

# generate primes to serve as "coins", so values available to be added
primes = generatePrimes(MAX)

# set the target and start for iterator
target = 5000
length = 1

# below program was adjusted from problem 31 and also 76
while True:
    ways = [0]*length
    ways.insert(0, 1)
    for x in primes:
        for i in range(x, length+1):
            ways[i] = ways[i] + ways[i-x]
    if ways[-1] > target:
        break
    length += 1
    
print(length)
