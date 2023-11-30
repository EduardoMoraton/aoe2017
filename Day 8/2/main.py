
data_path = './../input.txt'

class Operation:
    def __init__(self, data):
        arr = data.split(' ')
        self.reg = arr[0]
        self.operation_str = arr[1]
        self.val = arr[2]
        self.condition_reg_key = arr[4]
        self.operator = arr[5]
        self.condition_operator = arr[6].strip()
          
    def operate(self, registers, historic_max):
        if self.reg not in registers:
            registers[self.reg] = 0
        if self.condition_reg_key not in registers:
            registers[self.condition_reg_key] = 0
    
        str_condition = str(registers[self.condition_reg_key])+self.operator+self.condition_operator
        print(str_condition)
        if eval(str_condition):
            if self.operation_str == 'inc':
                registers[self.reg] += int(self.val)
            else:
                registers[self.reg] -= int(self.val) 
        if registers[self.reg] > historic_max:
            historic_max = registers[self.reg]
        return historic_max


registers = {}
operations = []




def read_data(path):
    lines = []
    with open(path, 'r') as file:
        lines = file.readlines()

    for line in lines:
        op = Operation(line)
        operations.append(op)

read_data(data_path)

historic_max = 0
for op in operations:
    historic_max = op.operate(registers, historic_max)

print(max(registers.values()))
print(historic_max)
