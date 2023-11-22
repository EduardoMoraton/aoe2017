import itertools
file_path = '../iput.txt'


data = ""
with open(file_path, "r") as file:
    data = file.readline()



total = 0
half = int(len(data)/2)


firstHalf, secondHalf = data[:half], data[half:]


for i in range(int(len(data)/2)):
    if (firstHalf[i]==secondHalf[i]):
        total += int(firstHalf[i])*2
            
print(total)
