class Variable():
    def __init__(self, vtype, value):
        self.type = vtype
        self.value = value


class Function():
    def __init__(self):
        self.sym_table = None


class SymbolTable():
    def __init__(self):
        data = {}
    def set(self):
        pass
    def get(self):
        pass