data_path = '../input.txt'
data_raw = ''

with open(data_path, 'r') as file:
    data_raw = file.readline()
arr_raw = data_raw.split('\t')

data = [int(str(num.replace('\n', ''))) for num in arr_raw]


past_conv = []

max_val_index = 0
curr_conv = data

iterations = 0

while data not in past_conv:    
    past_conv.append(data.copy())
    max_val = max(curr_conv)
    max_val_index = data.index(max_val)
    data[max_val_index] = 0
    index = max_val_index
    while max_val > 0:
        index += 1
        if index == len(data):
            index = 0
        data[index] += 1

        max_val -= 1
    iterations += 1
print(iterations)

            
                                  
        

