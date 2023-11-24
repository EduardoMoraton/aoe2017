from itertools import permutations as perm
data_path = '../input.txt'
    
with open(data_path, 'r') as file:
    lines = file.readlines()
    lines = [line.replace('\n', '').split(' ') for line in lines]

count = 0


def get_sorted(line):
    per = [''.join(sorted(word)) for word in line] 
    print(per)
    return per    

for line in lines:
    valid = True
    sorted_line = get_sorted(line)
    for word in sorted_line:
        if sorted_line.count(word) > 1:
            valid = False
    if valid:
        count += 1

print(count)
