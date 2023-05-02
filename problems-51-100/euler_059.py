# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 23:45:15 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=59

# import libraries
import itertools
import requests

# get the data and transform it to list on digits
data = requests.get('https://projecteuler.net/project/resources/p059_cipher.txt').text 
data = data.split(",")
input_list = list(map(int, data))

# create ascii dictionary
# asciiDict = {i: chr(i) for i in range(128)}

# create ascii dictionary for english lowercase letters
# asciiDictLower = {i: chr(i) for i in range(97, 123, 1)}

# in python XOR() is applied by using "^" between two numbers
# 2 ^ ord("A")

# initiate possible solutions
possible_solutions = {}

# generate all keys
all_keys = list(itertools.permutations('abcdefghijklmnopqrstuvwxyz', 3))

# initiate current key for the loop
current_key = 0


# try every key
for current_key in range(len(all_keys)):
    
    # zip every digit on the encrypted list with its key-part
    # multiply key to extend it's length to match length of encrypted text
    temp = list(zip(input_list, list(all_keys[current_key]) * int((len(input_list)/3))))
    
    # initiate output and decrypt traversing through every digit in the encrypted file
    output = ''
    for i in range(len(temp)):
        output = output + (chr(temp[i][0] ^ ord(temp[i][1])))
    
    # count how many digits in the output match one of the english letters or space
    count = 0
    for i in range(len(output)):
        if output[i] in ('abcdefghijklmnopqrstuvwxyz ABCDEFGHIJKOLMNOPQRSTUVWXYZ'):
            count += 1
    
    # if match rate is higher than 90%, add the output to the dictionary of possible solutions
    if count / len(output) > 0.9:
        possible_solutions[''.join(all_keys[current_key])] = output


# print all the possible solutions
print(len(possible_solutions))

for key, value in possible_solutions.items() :
    print ("KEY: \n", key, "\n\nTEXT:\n", value)



# initiate sum of asci
print(sum(map(ord, possible_solutions["exp"])))

