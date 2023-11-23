import numpy as np
from itertools import cycle

input_value = 312051

def get_pos(num):
    direc = {"right": [1, 0], "up": [0, 1], "left": [-1, 0], "down": [0, -1]}
    direc = {k: np.array(v) for k, v in direc.items()}

    dir_pool = cycle(direc.keys())

    size = 1
    curr_size = 0
    direction = "up"

    curr_dir = next(dir_pool)

    pos = [0, 0]
    for i in range(2, num + 1):
        pos += direc[curr_dir]
        curr_size += 1
        if curr_size == size:
            curr_dir = next(dir_pool)
            curr_size = 0
            if curr_dir == "right" or curr_dir == "left":
                size += 1
    return pos

def get_adj(pos):
    arr = []
    for i in range(pos[0] - 1, pos[0] + 2):
        for j in range(pos[1] - 1, pos[1] + 2):
            if i != pos[0] or j != pos[1]:
                arr.append(np.array([i, j]))
    return arr

def get_sum_from_pos(arr, adj):
    total_sum = 0
    for i in range(len(arr)):
        cal_pos = tuple(get_pos(i + 1))
        if cal_pos in map(tuple, adj):
            total_sum += arr[i]
            #print("POS:")
            #print(cal_pos)
    return total_sum


arr = [1]

for i in range(2, input_value):
    pos = get_pos(i)
    adj = get_adj(pos)
    sum = get_sum_from_pos(arr, adj)
    print(sum)
    arr.append(sum)
    
    if (arr[len(arr)-1]>input_value):
        print("SOLUCION")
        print(arr[len(arr)-1])
        break

