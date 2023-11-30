file_path = '../input.txt'

checksum = 0

with open(file_path, "r") as file:
    data = file.readlines()

def sum_of_evenly(l):
    
    for num in l:
        for other in l:
            if other != num:
                if num%other == 0:
                    return num/other

checksum = 0
for d in data:
    d = d.replace("\n", "")
    d = d.split("\t")
    d_int = [int(i) for i in d]
    checksum += sum_of_evenly(d_int)
    
d


print(int(checksum))  
