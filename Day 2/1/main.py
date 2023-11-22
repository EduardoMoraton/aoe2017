file_path = '../input.txt'

checksum = 0

with open(file_path, "r") as file:
    data = file.readlines()

for d in data:
    d = d.replace("\n", "")
    d = d.split("\t")
    d_int = [int(i) for i in d]
    diff = max(d_int) - min(d_int)
    checksum += diff

print(checksum)
