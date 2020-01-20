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
from utils.oasm_parser import parse


def decode_to_or1(code):
    result =[]

    if code[0] == "START":
        result.append(code[1])
        result.append(code[2])
    else:
        raise BaseException("file dont have defined start of main function")

    for item in code[3:]:
        if isinstance(item, str):
            result.append(instruction(item))
        else:
            result.append(item)
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
    #save_to_file(decode_or1(parse(read_from_file(arguments["<input>"]))),arguments)
    test ="""label1:
test
label2:
test 1 2 3 4
label4:
"""
    print(parse(test))