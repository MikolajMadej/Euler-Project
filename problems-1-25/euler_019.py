# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 15:27:06 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=19

# import datetime
import datetime 

# define start and end date
start = datetime.date(1901, 1, 1)
end = datetime.date(2000, 12, 31)

# calculate difference in days between start and end
periods = end-start
periods_num = periods.days

# 0 - monday
# 6 - sunday


# create a list of all sundays on the forst day of month
sundays_on_1st = []
for day in range(0, periods_num):
    current_date = start + datetime.timedelta(days = day)
    if current_date.weekday() == 6 and current_date.strftime("%d") == '01':
        sundays_on_1st.append(current_date)
        
        
# print number of sych sundays
len(sundays_on_1st)
