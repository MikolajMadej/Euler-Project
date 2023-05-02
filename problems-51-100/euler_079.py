# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 14:55:15 2023

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=79

# get data
import requests
data = requests.get("https://projecteuler.net/project/resources/p079_keylog.txt").text

# split to list
data = data.split("\n")
data.pop(len(data)-1)

# delete duplicates and sort
data = sorted(list(set(data)))

# split list into sublists
data_split = []
for num in data:
    data_split.append(list(num))

del data, num

# first, second and third digit
# first_digit = []
# secon_digit = []
# third_digit = []

# for code in data_split:
#     print(code)
#     first_digit.append(int(code[0]))
#     secon_digit.append(int(code[1]))
#     third_digit.append(int(code[2]))
    
# first_digit = list(set(first_digit))
# secon_digit = list(set(secon_digit))
# third_digit = list(set(third_digit))

# del code


# order
order = {}

# create a dictionary of pointers
# key is predecesor, values are numbers that need to be after it
for i in range(len(data_split)):
    if data_split[i][0] not in list(order.keys()):
        order[data_split[i][0]] = [data_split[i][1]]
    elif data_split[i][1] not in order[data_split[i][0]]:
        order[data_split[i][0]].append(data_split[i][1])
        

for i in range(len(data_split)):
    if data_split[i][1] not in list(order.keys()):
        order[data_split[i][1]] = [data_split[i][2]]
    elif data_split[i][2] not in order[data_split[i][1]]:
        order[data_split[i][1]].append(data_split[i][2])
        
        
final_key = ""
for key, value in zip(order.keys(), order.values()):
    if len(value) == 1:
        final_key = final_key + key + value[0]      
        break
    
del order[key]

for key, value in zip(order.keys(), order.values()):
    if final_key[0] in value:
        order[key].remove(final_key[0])
    if final_key[1] in value:
        order[key].remove(final_key[1])

del key, value, i


# ad recursion here ------------------------------------
# for key, value in zip(order.keys(), order.values()):
#     if len(value) == 0:
#         final_key = key + final_key      
#         break
    
# del order[key]

# for key, value in zip(order.keys(), order.values()):
#     if final_key[0] in value:
#         order[key].remove(final_key[0])

# print(final_key)

# -----------------------------------------------------

def shrink_dict(input_dict, input_key):

    for key, value in zip(input_dict.keys(), input_dict.values()):
        if len(value) == 0:
            input_key = key + input_key      
            break
        
    print(input_key)
    del input_dict[key]

    for key, value in zip(input_dict.keys(), input_dict.values()):
        if input_key[0] in value:
            input_dict[key].remove(input_key[0])

    if len(input_dict) > 0:
        shrink_dict(input_dict, input_key)


shrink_dict(order, final_key)

