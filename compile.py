# Authors: Marcus San Antonio, Christian Apostol
# Pledge: I pledge my honor that I have abided by the Stevens Honor System.
# CPU Name: Budget CPU
# Python Program that compiles assembly code into image files to be used in budget_cpu.circ

def read_assembly():
    """Reads each line as an individual instruction from assembly.txt and divides them into instruction and memory"""
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

    return format(int(binary_str, 2), '02x') # Convert binary instruction to hexadecimal

def compile_data(d):
    """Converts assembly data assignment into a tuple : (memory index, data value in hexadecimal)"""
    if len(d) == 5:
        memory_add = int(d[1])
        value = format(int(d[4]), '02x')
    else:
        memory_add = int(d[1:3])
        value = format(int(d[4:6]), '02x')
    return(memory_add, value)

def create_ins_img(instructions):
    """Takes an array of instructions and outputs image file for instruction_mem"""
    # Use dictionary with keys that are multiples of 16 - each represent a row in instruction_mem.txt
    output = {
        0: ['00'] * 16,
        16: ['00'] * 16,
        32: ['00'] * 16,
        48: ['00'] * 16,
        64: ['00'] * 16,
        80: ['00'] * 16,
        96: ['00'] * 16,
        112: ['00'] * 16,
        128: ['00'] * 16,
        144: ['00'] * 16,
        160: ['00'] * 16,
        176: ['00'] * 16,
        192: ['00'] * 16,
        208: ['00'] * 16,
        224: ['00'] * 16,
        240: ['00'] * 16,
    }

    count = 0 # Keeps track of index on current key
    cur_key = 0

    # Add instructions to the output dictionary
    for i in instructions:
        if count == 16: # Move to next key
            count = 0
            cur_key += 16 # Increment key value by 16
        output[cur_key][count] = i
        count += 1

    f = open("instruction_mem.txt", "w")
    f.write("v3.0 hex words addressed\n")

    # Iterate over each key and output its corresponding instruction list
    for key in output:
        f.write(format(key, '02x')) # Convert decimal key to hexadecimal string
        f.write(": ")
        for inst in output[key]:
            f.write(inst + " ")
        f.write("\n")
    f.close()

def create_data_img(data):
    """Takes an array of memory assignments and outputs image file"""
    f = open("data_mem.txt", "w")
    f.write("v3.0 hex words addressed\n")
    f.write("0: ")
    # Iterate over data values and output them to txt file
    for d in data:
        f.write(d + " ")
    f.write("\n")
    f.close()

if __name__ == "__main__":
    program = read_assembly() # Divide assembly into instruction and data segments
    create_ins_img(program[0]) # Output/Overwrite instruction_mem.txt
    create_data_img(program[1]) # Output/Overwrite data_men.txt