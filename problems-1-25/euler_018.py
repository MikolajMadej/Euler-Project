# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 15:23:35 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=18


# define the triangle
triangle = """
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23
"""

# transform triangle to a list (every row is a separate string in a list)
triangle_as_list = list(triangle.split("\n"))
triangle_as_list.pop()
triangle_as_list.pop(0)


# tansform every string (triangle row) to a list - we end up with a list of lists
list_in_list = [0] * len(triangle_as_list)

for row in range(0, len(triangle_as_list)):
    list_in_list[row] = triangle_as_list[row].split(" ")


# starting from triangle foundation summarise all adjacent pairs of numbers, take bigger pair and add to the corresponding
# node in row above
for row in range(14, 0, -1):
    current_row = [0] * (row)
    for element in range(row):
        current_row[element] = max(int(list_in_list[row][element]), int(list_in_list[row][element+1])) 
    for i in range(row):
        list_in_list[row-1][i] =  int(current_row[i]) + int(list_in_list[row-1][i])


# print the tip of the triangle
print(list_in_list[0][0])
