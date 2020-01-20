"""
OrvilleVM assembler.

Usage:
    oasm.py <input> <output> [-d]
    oasm.py -h | --help
    oasm.py -v | --version

Options:
  -h --help     Show this screen.
  -v --version  Show version.
"""
from bytecode import instruction
from docopt import docopt
from utils.oasm_parser import *


def create_symbol_table(code):
    table = {}
    index = 0
    while(index < len(code)):
        if isinstance(code[index], Label):
            table[code[index].value] = index - 1
            del code[index]
        index +=1
    return table, code



def decode(code,stable):
    result =[]

    if code[0].value == "START":
        result.append(code[1])
        result.append(code[2])
    else:
        raise BaseException("file dont have defined start of main function")

    for item in code[3:]:
        if isinstance(item, Keyword):
            result.append(instruction(item.value))
        elif isinstance(item, Var):
            result.append(stable[item.value])
        else:
            result.append(item)
    return result
    


def decode_to_or1(code):
    result = parse(string)
    result = create_symbol_table(result)
    result = decode(result[1],result[0])
    return result

def read_from_file(scr):
    with open(scr) as file:
        data = file.read()
    return data

def save_to_file(list, args):
    debug = args["-d"]
    if debug == True:
        src = args["<output>"]
        with open(src, "w") as file:
            for item in list:
                file.write(str(item))
                file.write(" ")
    else:
        print("binary mode is not implemented")


if __name__ == "__main__":
    #arguments = docopt(__doc__, version='OrvilleVM assembler 0.0.1')
    #save_to_file(decode_to_or1(parse(read_from_file(arguments["<input>"]))),arguments)

    string ="""#coment
START 0 0
label1:
ADD 
label2:
SUB 99 $label4
label4: 
MUL
    """
    print(decode_to_or1(string))
    