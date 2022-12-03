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

    # index 0 holds all the assembly instructions, index 1 holds all the data assignments
    return [instructions, data]


def compile_ins_img(instructions):
    """Takes an array of instructions and outputs image file (one for instruction_mem and one for data_mem)"""

def compile_data_img(data):
    """Takes an array of memory assignments and outputs image file"""

if __name__ == "__main__":
    program = read_assembly()
    #compile_ins_img(program[0])
    #compile_data_img(program[1])