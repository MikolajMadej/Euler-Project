# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 19:51:26 2023

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=81

import requests

# get the data and transform to list
df_data = requests.get('https://projecteuler.net/project/resources/p081_matrix.txt').text
df_data = df_data.split('\n')
df_data.pop(len(df_data)-1)

# nest lists in a list to get 80x80 split
df_data_fin = [list(map(int, row.split(','))) for row in df_data]

# get dimensions of "data frame"
rows, cols = len(df_data_fin), len(df_data_fin[0])

# minimum path sum from the top left corner to any given cell is the value of the cell 
# plus the minimum of the path sum to the cell above it and the path sum to the cell to the left of it
for i in range(1, rows):
    for j in range(1, cols):
        
        if j == 1:
            df_data_fin[i][0]+= df_data_fin[i-1][0]
            
        if i == 1:
            df_data_fin[0][j]+= df_data_fin[0][j-1]
            
        df_data_fin[i][j]+= min(df_data_fin[i-1][j], df_data_fin[i][j-1])
 
    
# print the result   
print(df_data_fin[-1][-1])

