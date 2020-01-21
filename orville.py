"""
OrvilleVM

Usage:
    orville.py oasm <input> [-d]
    orville.py or1 <input> [-d]

Options:
  -h --help     Show this screen.
  -v --version  Show version.
"""
from docopt import docopt
from oasm import *
from odisasm import parse_debug_or1
from vm import VM

def load_oasm(file):
    return decode_to_or1(parse(read_from_file(file)))

def load_or1(file):
    return 

if __name__ == "__main__":
    arguments = docopt(__doc__, version='OrvilleVM 0.0.1')
    #arguments = {"<input>":r".\examples\print_int.out", "-d":False,'oasm': False,'or1': True}
    if arguments["oasm"] == True:
        code = decode_to_or1(parse(read_from_file(arguments["<input>"])))
    elif arguments["or1"] == True: 
        code = parse_debug_or1(read_from_file(arguments["<input>"]))
    
    vm = VM(code[2:],code[0],code[1])
    if arguments["-d"] == True:
        vm.debug = True
    try:
        vm.cpu()
        if vm.debug == True:
            print(code)
            print(vm.trace)
    except BaseException as e:
        print(code)
        print(vm.trace)
        raise e