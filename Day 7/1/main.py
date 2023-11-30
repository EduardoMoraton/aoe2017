data_path = '../input.txt'

class Program:
    def __init__(self, name, children_names):
        self.name = name
        self.children_names = children_names
        self.children = []
        self.parent = None

    def is_child_name(self, name):
        return name in self.children_names

    def has_children_names(self):
        return len(self.children_names) >= 1

    def is_child(self, children):
        return children in self.children

    def has_children(self):
        return len(self.children) >= 1

    def has_parent(self): 
        return self.parent != None

    def add_child(self, child):
        self.children.append(child)

    def __str__(self):
        return str(self.name)
    
    def tree(self, indent=0):
        prefix = "    " * indent
        print(f"{prefix}|-- Parent: {self.parent}, Name: {self.name}")
        for child in self.children:
            child.tree(indent + 1)


def read_data(path):
    programs = []
    lines = []
    with open(path, 'r') as file:
        lines = file.readlines()
    for line in lines:
        a = line.split('->')
        name = a[0].split(' ')[0]
        children = []
        if len(a) > 1:
            children = a[1].split(', ')
            children = [child.replace(' ', '').replace('\n', '') for child in children]
        program = Program(name, children)
        programs.append(program)
    
    return programs
        

def calculate_children_names(programs):
    for program in programs:
        if program.has_children_names():
            for pro in programs:
                if program.is_child_name(pro.name):
                    program.add_child(pro)
    return programs

def calculate_parents(programs):
    for program in programs:
        if not program.has_parent():
            for pro in programs:
                if pro.is_child(program):
                    program.parent = pro
    return programs

programs = read_data(data_path)
programs = calculate_children_names(programs)
programs = calculate_parents(programs)


for program in programs:
    program.tree()
    if not program.has_parent():
        print(program)
