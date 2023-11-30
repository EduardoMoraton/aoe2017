data_path = '../input.txt'


with open(data_path, 'r') as file:
    data = file.readlines()
    data = [int(entry.replace('\n', '')) for entry in data]



steps = 0
current_index = 0
exit = False

while not exit:
    past_index = current_index
    instruction = data[current_index]
    current_index += instruction

    if current_index >= len(data):
        exit = True
    else:
         data[past_index] += 1
    steps += 1

print(steps)
