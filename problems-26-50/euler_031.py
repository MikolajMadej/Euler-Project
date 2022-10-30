# -*- coding: utf-8 -*-
"""
Created on Thu Oct 20 21:34:02 2022

@author: Mikolaj Madej
"""

# Problem link
# https://projecteuler.net/problem=31

# available coins: 1, 2, 5, 10, 20, 50, 100, 200
# how to make 200?

# 1) (take 1x200) or (0x200 andsome others)
# 2) (take 2x100) or (1x100 and some others) or (0x100 and some others)
# 3) (take 4x50) or (3x50 and some others) or (2x50 and some others) ...

# len(range(1)) is 1


import time

start = time.time()
counter = 0
# number of 200p coins
for x in range(1):
    
    # number of used 100p coins
    for a in range(3):
        
    	# number of used 50p coins
    		for b in range(int(1+(200-200*x+100*a)/50)):   # range is how many nickels are left
                
    			# number of used 20p coins
    				for c in range(int(1+(200-200*x-100*a-50*b)/20)):
                        
    					# number of used 10p coins
    						for d in range(int(1+(200-200*x-100*a-50*b-20*c)/10)):
                                
    							# number of used 5p coins
    								for e in range(int(1+(200-200*x-100*a-50*b-20*c-10*d)/5)):
                                        
    									# number of used 2p coins
    										for f in range(int(1+(200-200*x-100*a-50*b-20*c-10*d-5*e)/2)):
    											counter += 1
                                            
print(counter)

end = time.time()
print(end-start) #0.015s





# OR (adjusted from https://stackoverflow.com/questions/790606/understanding-project-euler-31)

start = time.time()

ways = [0]*201
ways[0] = 1
for x in [1,2,5,10,20,50,100,200]:
    for i in range(x, 201):
        ways[i] = ways[i] + ways[i-x]

print(ways[200])

end = time.time()
print(end-start) #0.0s
