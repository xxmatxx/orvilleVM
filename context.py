class Context():
    def __init__(self, returnip, nlocals):
        self.returnip = returnip
        self.locals = [None] * nlocals