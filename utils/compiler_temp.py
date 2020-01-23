class integer_inst():
    def __init__(self,integer):
        self.int = integer
    
    def to_string(self):
        return "PUSH " + str(self.int) + "\n"


class primitive_inst():
    def __init__(self, *args):
        self.fn = args[0]
        self.args = args[1:]

    def to_string(self):
        return ""

class SymbolTable():
    def __init__(self):
        data = {}
    def set(self):
        pass
    def get(self):
        pass


class Function():
    def __init__(self):
        self.sym_table = None



class Variable():
    def __init__(self, vtype, value):
        self.type = vtype
        self.value = value