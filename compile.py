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

    # Decode each instruction to hexadecimal values
    for i, inst in enumerate(instructions):
        instructions[i] = compile_ins(inst)

    # Decoded each data assignment to hexadecimal values
    data_assignment = ['00'] * 16
    for i, da in enumerate(data):
        data[i] = compile_data(da)
        data_assignment[data[i][0]] = data[i][1]
    
    print(instructions)
    print(data_assignment)

    # index 0 holds all the assembly instructions, index 1 holds all the data assignments
    return [instructions, data_assignment]

def compile_ins(i):
    """Converts assembly instruction into hex code"""
    binary_str = ""

    # LDR decoding
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

    # Arithmetic decoding
    elif (i[0:3].lower() == "add" or i[0:3].lower() == "sub"):
        if (i[0:3].lower() == "add"):
            binary_str += "00"
        elif(i[0:3].lower() == "sub"):
            binary_str += "01"

        # Decode ReadReg2
        binary_str += format(int(i[11]), '02b')

        # Decode ReadReg1
        binary_str += format(int(i[8]), '02b')

        # Decode Destination Register
        binary_str += format(int(i[5]), '02b')

    return format(int(binary_str, 2), '02x') # Convert binary to hexadecimal

def compile_data(d):
    """Converts assembly data assignment into tuple pairs (memory index, data value in hex)"""
    if len(d) == 5:
        memory_add = int(d[1])
        value = format(int(d[4]), '02x')
    else:
        memory_add = int(d[1:3])
        value = format(int(d[4:6]), '02x')
    return(memory_add, value)

def create_ins_img(instructions):
    """Takes an array of instructions and outputs image file (one for instruction_mem and one for data_mem)"""
    f = open("test_i.txt", "w")
    f.write("v3.0 hex words addressed\n")
    f.close()

def create_data_img(data):
    """Takes an array of memory assignments and outputs image file"""
    f = open("data_mem.txt", "w")
    f.write("v3.0 hex words addressed\n")
    f.write("0: ")
    for d in data:
        f.write(d + " ")
    f.write("\n")
    f.close()

if __name__ == "__main__":
    program = read_assembly()
    create_ins_img(program[0])
    create_data_img(program[1])

    compile_ins('ADD R2 R1 R0')
    compile_ins('SUB R3 R0 R1')

    compile_data('M0: 4')
    compile_data('M12: 3')