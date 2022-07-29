from codecs import decode
import sys
# load the assembly file
codeFilePath = sys.argv[1]

with open(codeFilePath) as f:
    lines = f.readlines()
    

# the binary file to create
binFilePath = codeFilePath.replace(".asm", ".bin")
# binfile = "./" + "".join(codeFilePath.split('.')[0:-2]) + ".bin"

# map from instruction to binary
bin_map = {
    "wait": 0,
    "import": 1,
    "waste": 2,
    "store": 3,
    "pick": 4,
    "label": 5,
    "move": 6,
    "scan": 7
}

# operationmap
op_map = {
    "eq": 5
}

# valuetypes
valtypes = {
    "int": 0,
    "fork": 1,
    "label": 2
}

# define the reserved keywords as a combination of all the keys from the language.
keywords = op_map.keys() + bin_map.keys() + valtypes.keys()

# map of set labels to int location
label_map = {}

def decode_binmap(arg):
    if arg in bin_map.keys():
        return bin_map[arg]
    else:
        raise Exception(f"argument: '{arg}' not found in binmap!")

def decode_labelmap(lbl):
    if lbl in label_map.keys():
        return label_map[lbl]
    else:
        raise ValueError(f"Label: '{lbl}' not foumd in labelmap!")

def decode_opmap(op):
    if op in op_map.keys():
        return op_map[op]
    else:
        raise Exception(f"operation:'{op}' not found in opmap!")

class Forklift:
    def __init__(self, _loc):
        self.loc = _loc

    def move(self, loc):
        self.loc = loc

class Scanner:
    def niet(a):
        return not a

    def eq(a, b):
        return a == b
    
    

# list of binary instructions to be saved into binary file
bin_instr = []

# track what line we are on
line_tracker = 0

# the forklift sim for label instructions
fl = Forklift(0)

# fetch the instructions

# first pass finding the label instructions
for instr in lines:
    line_tracker += 1

    args = instr.split()
    assert len(args) > 0, "gimme some instructions"

    match args[0]:
        case "label":
            assert len(args) == 2, f"{args[0]} should have a name"
            if args[1].isdigit():
                raise ValueError(f"Line: '{line_tracker}' label name cannot be an int")
            if args[1] in keywords:
                raise ValueError(f"Line: '{line_tracker}' label cannot be one of the keywords in the language")
            else:
                label_map[args[1]] = -1

line_tracker = 0

# second pass going over all other instructions
for instr in lines:

    print(instr)
    line_tracker += 1
    print(instr.split())
    args = instr.split()
    assert len(args) > 0, "gimme some instructions"
    match args[0]:
        case "wait":
            bin_instr.append(decode_binmap(args[0]))
        case "import":
            bin_instr.append(decode_binmap(args[0]))
        case "waste":
            bin_instr.append(decode_binmap(args[0]))
        case "store":
            bin_instr.append(decode_binmap(args[0]))
            assert len(args) == 2, f"{args[0]} should have a int or a label reference"
            if args[1].isdigit():
                args[1] = int(args[1])
            if isinstance(args[1], int):
                bin_instr.append(args[1])
            elif isinstance(args[1], str):
                bin_instr.append(decode_labelmap(args[1]))
            else:
                raise ValueError(f"Line: {line_tracker} datatype argument '{args[0]}' instruction not handled!")
        case "pick":
            bin_instr.append(decode_binmap(args[0]))
        case "label":
            bin_instr.append(decode_binmap(args[0]))
            label_map[args[1]] = fl.loc

        case "move":
            bin_instr.append(decode_binmap(args[0]))
            assert len(args) == 2, f"{args[0]} should have a int or a label reference"
            if args[1].isdigit():
                args[1] = int(args[1])
            if isinstance(args[1], int):
                bin_instr.append(args[1])
                fl.move(args[1])
            elif isinstance(args[1], str):
                bin_instr.append(decode_labelmap(args[1]))
                fl.move(decode_labelmap(args[1]))
            else:
                raise ValueError(f"Line: {line_tracker} datatype argument '{args[0]}' instruction not handled!")
        case "scan":
            bin_instr.append(decode_binmap(args[0]))
            assert len(args) >= 3, "Scan needs 3 or more arguments"
            bin_instr.append(decode_opmap(args[1])) # parse the operation

            # parse the arguments
            for x in args[2:]:
                # parse the type
                bin_instr.append
            
        case _:
            raise Exception(f"Line: {line_tracker} this instruction is not understood!")
    
# convert to binary list
export = bytes(bin_instr)
print(export)

# write the binary
with open(binFilePath, "wb") as f:
    f.write(export)
