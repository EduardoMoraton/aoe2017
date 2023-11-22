import itertools
file_path = '../input.txt'


data = ""
with open(file_path, "r") as file:
    data = file.readline()



total = 0
for i in range(len(data)):
    curr = data[i]
    if i != len(data)-1:
        next = data[i+1]
    else:
        next = data[0]
    print("curr: " + curr)
    print("next: " + next)
    
    if curr == next:
        total += int(curr)
        
print(total)
