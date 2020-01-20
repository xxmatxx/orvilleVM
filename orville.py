"""
OrvilleVM

Usage:
    orville.py <input> [-d]

Options:
  -h --help     Show this screen.
  -v --version  Show version.
"""
from docopt import docopt
from oasm import *
from vm import VM

if __name__ == "__main__":
    arguments = docopt(__doc__, version='OrvilleVM 0.0.1')
    code = decode_to_or1(parse(read_from_file(arguments["<input>"])))
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