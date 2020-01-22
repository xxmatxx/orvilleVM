class Variable():
    def __init__(self, vtype, value):
        self.type = vtype
        self.value = value


class Function():
    def __init__(self):
        self.stable = None


class SymbolTable():
    def __init__(self):
        data = {}
    def set(self):
        pass
    def get(self):
        pass


class Compiler():
    def __init__(self):
        self.result = ""


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
        temp = ast.copy()
        temp.reverse()
        result = ""
        for ast in temp:
            if isinstance(ast, list):
                result += self.compile_form(ast)
            elif isinstance(ast, str):
                result += self.compile_primitive(ast)
            elif isinstance(ast, int):
                result += self.compile_int(ast)
        return result

    def compile(self,ast):
        if isinstance(ast, list):
            result = self.compile_form(ast)
        elif isinstance(ast, str):
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





c = Compiler()
result = c.run(5)
print(result)

# 5

#(+ 10 5)

#(+ (+ 5 5) 5)
#(+ (+ 10 6) (+ 5 8))
#(- 10 (+ 5 (/ 12 (* 6 2))))

#(def x 10)

#(lambda (a b) (+ a b) )