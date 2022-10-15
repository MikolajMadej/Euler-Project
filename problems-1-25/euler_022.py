# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 12:15:03 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=22


# import data (requests package allows to send HTTP request to pull web data).  
import requests
data = requests.get('https://projecteuler.net/project/resources/p022_names.txt').text

# transfor to sorted list of name strings
data_list = data.replace('"', '').split(",")
data_list.sort()

# define letter-to-number dictionary
dict_let_to_num = {'A': 1, 
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5,
    'F': 6,
    'G': 7,
    'H': 8,
    'I': 9,
    'J': 10,
    'K': 11,
    'L': 12,
    'M': 13,
    'N': 14,
    'O': 15,
    'P': 16,
    'Q': 17,
    'R': 18,
    'S': 19,
    'T': 20,
    'U': 21,
    'V': 22,
    'W': 23,
    'X': 24,
    'Y': 25,
    'Z': 26,
}


# declare to sum variable with 0 assigned as current value
total_sum = 0

# count sum of letters in names
for i in range(len(data_list)):
    current_name = list(data_list[i])                                          # transform every name to list of letters
    translated_list = list(map(dict_let_to_num.get, current_name))             # apply the dictionary to get nummeric representations of letters
    list_value = (i + 1) * sum(translated_list)                                # sum the letters in a name and multiply by ID
    total_sum = total_sum + list_value                                         # add current name value to total sum

# print output sum
print(total_sum)

