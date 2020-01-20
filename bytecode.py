bytecode = {
    "ADD":{"opcode":1,"narg":0},
    "SUB":{"opcode":2,"narg":0},
    "MUL":{"opcode":3,"narg":0},
    "DIV":{"opcode":4,"narg":0},
    "MOD":{"opcode":5,"narg":0},
    "JMP":{"opcode":6,"narg":1},
    "JEQ":{"opcode":7,"narg":1},
    "JNE":{"opcode":8,"narg":1},
    "PUSH":{"opcode":9,"narg":1},
    "POP":{"opcode":10,"narg":0},
    "SWAP":{"opcode":11,"narg":0},
    "DUP":{"opcode":12,"narg":0},
    "LOAD":{"opcode":13,"narg":1},
    "GLOAD":{"opcode":14,"narg":1},
    "STORE":{"opcode":15,"narg":1},
    "GSTORE":{"opcode":16,"narg":1},
    "PRINT":{"opcode":17,"narg":0},
    "FRAME":{"opcode":18,"narg":1},
    "CALL":{"opcode":19,"narg":2},
    "RET":{"opcode":20,"narg":0},
    "HALT":{"opcode":21,"narg":0}
}

class Context():
    def __init__(self, returnip, nlocals):
        self.returnip = returnip
        self.locals = [None] * nlocals

def instruction(str):
    return bytecode[str]["opcode"]

def opcode(i):
    for key,value in bytecode.items():
        if value["opcode"] == i:
            return (key,value["narg"])

def is_True(i):
    return i > 0


def is_False(i):
    return i <= 0