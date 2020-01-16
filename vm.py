from bytecode import instruction
class VM ():
    def __init__(self, code, main, datasize):
        self.data = [None] * datasize
        self.code = code
        self.stack = [None] * 1000
        self.ip = main
        self.sp = -1
        self.fp = -1
    
    def cpu(self):
        while self.ip < len(self.code):
            opcode = self.code[self.ip]
            self.ip += 1
            if opcode == instruction("ICONST"):
                value = self.code[self.ip]
                self.ip +=1
                self.sp +=1
                self.stack[self.sp] = value
            if opcode == instruction("PRINT"):
                value = self.stack[self.sp]
                self.sp -= 1
                print(value)
            if opcode == instruction("HALT"):
                return


def main():
    code = [
    instruction("ICONST"),99,
    instruction("PRINT"),
    instruction("HALT")
    ]
    vm = VM(code,0,0)
    vm.cpu()
    

if __name__ == "__main__":
    main()