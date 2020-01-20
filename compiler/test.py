#(def x 10)

class Variable():
    def __init__(self, vtype, value):
        self.type = vtype
        self.value = value


class Function():
    def __init__(self):
        self.stable = None

class SymbolTable():
    def __init__(self):
        pass
    def set(self):
        pass
    def get(self):
        pass




def compile(ast):
    pass

#(+ 10 5)

#(+ (+ 5 5) 5)
#(+ (+ 10 6) (+ 5 8))
#(- 10 (+ 5 (/ 12 (* 6 2))))


#(lambda (a b) (+ a b) )