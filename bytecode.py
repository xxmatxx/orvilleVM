bytecode = {
    "IADD":{"opcode":1,"narg":0},
    "ISUB":{"opcode":2,"narg":0},
    "IMUL":{"opcode":3,"narg":0},
    "ILT":{"opcode":4,"narg":0},
    "IEQ":{"opcode":5,"narg":0},
    "BR":{"opcode":6,"narg":1},
    "BRT":{"opcode":7,"narg":1},
    "BRF":{"opcode":8,"narg":1},
    "ICONST":{"opcode":9,"narg":1},
    "LOAD":{"opcode":10,"narg":1},
    "GLOAD":{"opcode":11,"narg":1},
    "STORE":{"opcode":12,"narg":1},
    "GSTORE":{"opcode":13,"narg":1},
    "PRINT":{"opcode":14,"narg":0},
    "POP":{"opcode":15,"narg":0},
    "HALT":{"opcode":16,"narg":0}
}

def instruction(str):
    return bytecode[str]["opcode"]

def opcode(i):
    for key,value in bytecode.items():
        if value["opcode"] == i:
            return (key,value["narg"])

def is_True(i):
    return i > 0


def is_False(i):
    return i == 0