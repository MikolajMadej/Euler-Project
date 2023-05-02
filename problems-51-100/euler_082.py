# -*- coding: utf-8 -*-
"""
Created on Sat Apr  1 15:43:26 2023

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=82

import requests

# get the data and transform to list
df_data = requests.get('https://projecteuler.net/project/resources/p082_matrix.txt').text
df_data = df_data.split('\n')
df_data.pop(len(df_data)-1)

# nest lists in a list to get 80x80 split
df_data_fin = [list(map(int, row.split(','))) for row in df_data]


# get dimensions of "data frame"
rows, cols = len(df_data_fin), len(df_data_fin[0])

# get the first column of data frame
previous = [df_data_fin[row][0] for row in range(rows)]

# update every column while already knowing the updated cost of path from previous column
# so let's iterate through every column of data frame
for column in range(1, cols):
    
    # get the current coumn and copy it
    current = [df_data_fin[row][column] for row in range(rows)]
    updated = current[:]
    
    # for every row in current column check costs of all the possible paths leading to it
    for row in range(0, rows):
        
        # check direct path (so value directly on the left - remenber that all values on the left are already updated)
        choices = [previous[row]]
        
        # check every path coming from up
        # there is a coupple of them, because starting point in previous column can be in every row
        for partial_up in range(0, row, 1):
            choices.append(previous[partial_up]+sum(current[partial_up:row]))
        
        # check every path coming from down
        for partial_do in range(rows-1, row, -1):
            choices.append(previous[partial_do]+sum(current[row+1:partial_do+1]))
        
        # get the cheapest path and update current row
        updated[row] += min(choices) 
    
    # when all the rows are updated, overwrite the previous row with the current updated one
    previous = updated[:]

# print the result
min(previous)






