from bytecode import instruction, is_False, is_True
from bytecode import opcode as from_opcode
class VM ():
    DEFAULT_STACK_SIZE = 1000
    DEFAULT_CALL_STACK_SIZE = 1000
    def __init__(self, code, main, datasize):
        self.globals = [None] * datasize

        self.code = code
        self.stack = [None] * VM.DEFAULT_STACK_SIZE
        self.callstack = [None] * VM.DEFAULT_CALL_STACK_SIZE

        self.ip = main
        self.sp = -1
        self.callsp = 1

        self.debug = True
        self.trace = "--------------------------------------\n"
        self.h = -1
    def _globals_dumps(self):
        self.trace += "--------------------------------------\nData memory:\n--------------------------------------\n"
        adr_format = '{:>03}'
        for i in range(len(self.globals)):
            if self.globals[i] != None:
                address = adr_format.format(i)
                value = str(self.globals[i])
                self.trace += address + ":\t" + value + "\n"


    def _add_trace(self, opcode):
        adr_format = '{:>03}'
        address = adr_format.format(str(self.ip - from_opcode(opcode)[1] - 1))
        trace_opcode = from_opcode(opcode)[0]
        args = str(self.code[self.ip-1])
        stack = str(self.stack[:self.sp + 1])
        if(from_opcode(opcode)[1] == 0):
            self.trace = self.trace +address + " : "+ trace_opcode + "\t\t" +  stack + "\n"
        if(from_opcode(opcode)[1] == 1):
            self.trace = self.trace +address + " : "+ trace_opcode + "\t"+ args + "\t" + stack + "\n"

    def cpu(self):
        while self.ip < len(self.code) and self.h != 0:
            opcode = self.code[self.ip]
            self.ip += 1
            if opcode == instruction("ICONST"):
                value = self.code[self.ip]
                self.ip += 1
                self.sp += 1
                self.stack[self.sp] = value
            if opcode == instruction("IADD"):
                value2 = self.stack[self.sp]
                self.sp -= 1
                value1 = self.stack[self.sp]
                self.sp -= 1
                result = value1 + value2
                self.sp += 1
                self.stack[self.sp] = result
            if opcode == instruction("ISUB"):
                value2 = self.stack[self.sp]
                self.sp -= 1
                value1 = self.stack[self.sp]
                self.sp -= 1
                result = value1 - value2
                self.sp += 1
                self.stack[self.sp] = result
            if opcode == instruction("IMUL"):
                value2 = self.stack[self.sp]
                self.sp -= 1
                value1 = self.stack[self.sp]
                self.sp -= 1
                result = value1 * value2
                self.sp += 1
                self.stack[self.sp] = result
            if opcode == instruction("ILT"):
                value2 = self.stack[self.sp]
                self.sp -= 1
                value1 = self.stack[self.sp]
                self.sp -= 1
                result = int(value1 < value2)
                self.sp += 1
                self.stack[self.sp] = result
            if opcode == instruction("IEQ"):
                value2 = self.stack[self.sp]
                self.sp -= 1
                value1 = self.stack[self.sp]
                self.sp -= 1
                result = int(value1 == value2)
                self.sp += 1
                self.stack[self.sp] = result
            if opcode == instruction("BR"):
                self.ip = self.code[self.ip]
            if opcode == instruction("BRT"):
                addr = self.code[self.ip]
                value = self.stack[self.sp]
                self.sp -= 1
                if(is_True(value)):
                    self.ip = addr
            if opcode == instruction("BRF"):
                addr = self.code[self.ip]
                value = self.stack[self.sp]
                self.sp -= 1
                if(is_False(value)):
                    self.ip = addr
            if opcode == instruction("GSTORE"):
                value = self.stack[self.sp]
                self.sp -= 1
                addr = self.code[self.ip]
                self.ip += 1
                self.globals[addr] = value
            if opcode == instruction("GLOAD"):
                addr = self.code[self.ip]
                self.ip += 1
                value = self.globals[addr]
                self.sp += 1
                self.stack[self.sp] = value
            if opcode == instruction("POP"):
                self.sp -= 1
            if opcode == instruction("PRINT"):
                value = self.stack[self.sp]
                self.sp -= 1
                print(value)
            if opcode == instruction("HALT"):
                self.h = 0
            if(self.debug):
                self._add_trace(opcode)
        if(self.debug):
            self._globals_dumps()
        return self.h


def main():
    code = [
    instruction("ICONST"),11,
    instruction("ICONST"),10,
    instruction("ILT"),
    instruction("GSTORE"),0,
    ]
    vm = VM(code,0,10)
    vm.cpu()
    if vm.debug == True:
        print(vm.trace)
    

if __name__ == "__main__":
    main()