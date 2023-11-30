import numpy as np
from itertools import cycle

input = 312051


direc = { "right" : [1,0], "up": [0,1], "left": [-1, 0], "down": [0,-1] }


direc = {k:np.array(v) for k, v in direc.items()}
print(direc.keys())

dir_pool = cycle(direc.keys())

size = 1
curr_size = 0
direction = "up"

curr_dir =  next(dir_pool)


pos = [0,0]
for i in range(2, input+1):
    pos += direc[curr_dir]
    curr_size += 1
    if curr_size == size:
        curr_dir = next(dir_pool)
        curr_size = 0
        if curr_dir == "right" or curr_dir == "left":
            size += 1
        
                   
print(pos)
print(abs(pos[0])+abs(pos[1]))    
