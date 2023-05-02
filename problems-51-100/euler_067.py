# -*- coding: utf-8 -*-
"""
Created on Tue Jan 24 21:25:34 2023

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=67

# import data
import requests
data = requests.get("https://projecteuler.net/project/resources/p067_triangle.txt").text

# transform triangle to a list (every row is a separate string in a list)
triangle_as_list = list(data.split("\n"))
triangle_as_list.pop()

# tansform every string (triangle row) to a list - we end up with a list of lists
list_in_list = [0] * len(triangle_as_list)

for row in range(0, len(triangle_as_list)):
    list_in_list[row] = triangle_as_list[row].split(" ")
    
    
    
# starting from triangle foundation summarise all adjacent pairs of numbers, take bigger pair and add to the corresponding
# node in row above
for row in range(99, 0, -1):
    current_row = [0] * (row)
    for element in range(row):
        current_row[element] = max(int(list_in_list[row][element]), int(list_in_list[row][element+1])) 
    for i in range(row):
        list_in_list[row-1][i] =  int(current_row[i]) + int(list_in_list[row-1][i])


# print the tip of the triangle
print(list_in_list[0][0])