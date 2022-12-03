def read_assembly():
    """Reads each line as an individual instruction from assembly.txt and returns them in an array"""
    with open('assembly.txt') as f:
        assembly = [line.rstrip() for line in f] # Strip '\n' from each line

    assembly.remove("") # Trim all empty lines from the instruction
    for i, line in enumerate(assembly):
        if line == "DATA": # Identify the data break
            # Use list indexing to divide
            instructions = assembly[0:i]
            data = assembly[i+1:len(assembly)]
    print(instructions)
    print(data)

    #for i, inst in enumerate(instructions):
    #    instructions[i] = compile_ins(inst)

    # index 0 holds all the assembly instructions, index 1 holds all the data assignments
    return [instructions, data]

def compile_ins(i):
    binary_str = ""

    if i[0:3].lower() == "ldr":
        binary_str += ("10")

        # Decode memory address
        if (len(i) == 9):
            memory_add = i[8]
        else:
            memory_add = i[8:10]
        binary_str += format(int(memory_add), '04b') # Pad to make output 4 bits

        # Decode destination register
        binary_str += format(int(i[5]), '02b')

    elif i[0:3].lower() == "add":
        binary_str += ("00")
    elif i[0:3].lower() == "sub":
        binary_str += ("01")

    print(binary_str)

def create_ins_img(instructions):
    """Takes an array of instructions and outputs image file (one for instruction_mem and one for data_mem)"""
    f = open("test_i.txt", "w")
    f.write("v3.0 hex words addressed\n")
    f.close()

def create_data_img(data):
    """Takes an array of memory assignments and outputs image file"""


    f = open("test_d.txt", "w")
    f.write("v3.0 hex words addressed\n")
    f.close()

if __name__ == "__main__":
    program = read_assembly()
    create_ins_img(program[0])
    create_data_img(program[1])

    compile_ins('LDR R0 M0')
    compile_ins('LDR R1 M1')