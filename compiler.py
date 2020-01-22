"""
Lisp compiler for OrvilleVM

Usage:
    compiler.py <input> <output>
    compiler.py -h | --help
    compiler.py -v | --version

Options:
  -h --help     Show this screen.
  -v --version  Show version.
"""
from utils.lisp_parser import read_str as parse,Symbol
from utils.io import read_from_file
from docopt import docopt


class Compiler():
    def __init__(self):
        pass


    def compile_int(self,i):
        return "PUSH " + str(i) + "\n"


    def compile_primitive(self, p):
        if p == "+":
            return "ADD\n"
        if p == "-":
            return "SUB\n"
        if p == "*":
            return "MUL\n"
        if p == "/":
            return "DIV\n"
        if p == "mod":
            return "MOD\n"


    def compile_header(self, start, memory):
        return "START " + str(start) + " " + str(memory)+ "\n"


    def compile_footer(self):
        return "PRINT\n"

    

    def compile_form(self,ast):
        result = ""
        temp = ast.copy()
        temp.reverse()
        for ast in temp:
            if isinstance(ast, list):
                result += self.compile_form(ast)
            elif isinstance(ast, Symbol):
                result += self.compile_primitive(ast)
            elif isinstance(ast, int):
                result += self.compile_int(ast)
        return result

    def compile(self,ast):
        result = ""
        if isinstance(ast, list):
            result = self.compile_form(ast)
        elif isinstance(ast, Symbol):
            result = self.compile_primitive(ast)
        elif isinstance(ast, int):
            result = self.compile_int(ast)
        return result

    def run(self, ast):
        result = ""
        result += self.compile_header(0,0)
        result += self.compile(ast)
        result += self.compile_footer()
        return result




if __name__ == "__main__":
    arguments = docopt(__doc__, version='OrvilleVM assembler 0.0.1')
    c = Compiler()
    
    code = read_from_file(arguments["<input>"])
    print(code)
    ast = parse(code)
    print(ast)
    result = c.run(ast)
    print(result)

# 5

#(+ 10 5)

#(+ (+ 5 5) 5)
#(+ (+ 10 6) (+ 5 8))
#(- 10 (+ 5 (/ 12 (* 6 2))))

#(def x 10)

#(lambda (a b) (+ a b) )