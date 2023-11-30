data_path = '../input.txt'
    
with open(data_path, 'r') as file:
    lines = file.readlines()
    lines = [line.replace('\n', '').split(' ') for line in lines]

count = 0

for line in lines:
    valid = True
    for word in line:
        if line.count(word) > 1:
            valid = False
    if valid:
        count += 1

print(count)


