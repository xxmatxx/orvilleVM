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

from parsy import char_from, regex, char_from, generate
from bytecode import instruction
from docopt import docopt

whitespace1p = char_from("\n\r\t ").desc("at lest 1 white space character").at_least(1)
whitespace0p = char_from("\n\r\t ").desc("zero or more white space characters").many()

keywordp = regex(r"[a-zA-Z]+").desc("keyword")
integerp = regex(r"-?\d+").map(int).desc("integer")
commentp = regex(r"#.*").map(lambda a: []).desc("commen")

@generate
def argp():
    yield whitespace1p
    result = yield integerp
    return result

@generate
def line():
    result1 = yield keywordp
    result2 = yield argp.many()
    yield whitespace0p
    yield commentp.at_least(0)
    yield whitespace0p
    return [result1] + result2

@generate
def lines():
    result = yield line.many()
    flat_result = [item for sublist in result for item in sublist]
    return flat_result


def parse(string):
    return lines.parse(string)

def decode(list):
    result =[]
    for item in list:
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
    arguments = docopt(__doc__, version='OrvilleVM assembler 0.0.1')
    save_to_file(decode(parse(read_from_file(arguments["<input>"]))),arguments)