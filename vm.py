from bytecode import instruction, is_False, is_True, Context
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
        self.callsp = -1

        self.debug = False
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


    def _trace_address(self):
        address = '{:>03}'.format(str(self.ip))
        self.trace = self.trace + address + " : "
    
    def _trace_opcode(self,opcode):
        trace_opcode = from_opcode(opcode)[0]
        self.trace = self.trace + trace_opcode
    
    def _trace_args(self,opcode):
        if(from_opcode(opcode)[1] == 0):
            self.trace = self.trace + "\t\t"
        if(from_opcode(opcode)[1] == 1):
            arg1 = str(self.code[self.ip+1])
            self.trace = self.trace+ "\t"+ arg1 + "\t"
        if(from_opcode(opcode)[1] == 2):
            arg2 = str(self.code[self.ip+2])
            arg1 = str(self.code[self.ip+1])
            self.trace = self.trace + "\t" + arg1 +" "+ arg2 + "\t"  
        
    def _trace_stack(self):
        stack = str(self.stack[:self.sp + 1])
        self.trace = self.trace  +stack + "\n"

    def cpu(self):
        while self.ip < len(self.code) and self.h != 0:
            opcode = self.code[self.ip]
            if(self.debug):
                self._trace_address()
                self._trace_opcode(opcode)
                self._trace_args(opcode)
            self.ip += 1
            if opcode == instruction("PUSH"):
                value = self.code[self.ip]
                self.ip += 1
                self.sp += 1
                self.stack[self.sp] = value
            elif opcode == instruction("ADD"):
                value2 = self.stack[self.sp]
                self.sp -= 1
                value1 = self.stack[self.sp]
                self.sp -= 1
                result = value1 + value2
                self.sp += 1
                self.stack[self.sp] = result
            elif opcode == instruction("SUB"):
                value2 = self.stack[self.sp]
                self.sp -= 1
                value1 = self.stack[self.sp]
                self.sp -= 1
                result = value1 - value2
                self.sp += 1
                self.stack[self.sp] = result
            elif opcode == instruction("MUL"):
                value2 = self.stack[self.sp]
                self.sp -= 1
                value1 = self.stack[self.sp]
                self.sp -= 1
                result = value1 * value2
                self.sp += 1
                self.stack[self.sp] = result
            elif opcode == instruction("DIV"):
                value2 = self.stack[self.sp]
                self.sp -= 1
                value1 = self.stack[self.sp]
                self.sp -= 1
                result = value1 // value2
                self.sp += 1
                self.stack[self.sp] = result
            elif opcode == instruction("MOD"):
                value2 = self.stack[self.sp]
                self.sp -= 1
                value1 = self.stack[self.sp]
                self.sp -= 1
                result = value1 % value2
                self.sp += 1
                self.stack[self.sp] = result
            elif opcode == instruction("JMP"):
                self.ip = self.code[self.ip]
            elif opcode == instruction("JEQ"):
                addr = self.code[self.ip]
                self.ip += 1
                if is_True(self.stack[self.sp]):
                    self.ip = addr
                self.sp -= 1
            elif opcode == instruction("JNE"):
                addr = self.code[self.ip]
                self.ip += 1
                if is_False(self.stack[self.sp]):
                    self.ip = addr
                self.sp -= 1
            elif opcode == instruction("GSTORE"):
                value = self.stack[self.sp]
                self.sp -= 1
                addr = self.code[self.ip]
                self.ip += 1
                self.globals[addr] = value
            elif opcode == instruction("GLOAD"):
                addr = self.code[self.ip]
                self.ip += 1
                value = self.globals[addr]
                self.sp += 1
                self.stack[self.sp] = value
            elif opcode == instruction("LOAD"):
                regnum = self.code[self.ip]
                self.ip += 1
                self.sp += 1
                self.stack[self.sp] = self.callstack[self.callsp].locals[regnum]
            elif opcode == instruction("STORE"):
                regnum = self.code[self.ip]
                self.ip += 1
                self.callstack[self.callsp].locals[regnum] = self.stack[self.sp]
                self.sp -= 1
            elif opcode == instruction("POP"):
                self.sp -= 1
            elif opcode == instruction("SWAP"):
                temp = self.stack[self.sp]
                self.stack[self.sp] = self.stack[self.sp - 1]
                self.stack[self.sp - 1] = temp
            elif opcode == instruction("DUP"):
                value = self.stack[self.sp]
                self.sp += 1
                self.stack[self.sp] = value
            elif opcode == instruction("FRAME"):
                nlocals = self.code[self.ip]
                self.ip += 1
                self.callsp += 1
                self.callstack[self.callsp] = Context(-1, nlocals)
            elif opcode == instruction("CALL"):
                addr = self.code[self.ip]
                self.ip += 1
                nagrs = self.code[self.ip]
                self.ip += 1
                self.callstack[self.callsp].returnip = self.ip
                first_arg = self.sp - nagrs + 1
                for i in range(nagrs):
                    self.callstack[self.callsp].locals[i] = self.stack[first_arg+i]
                self.sp -= nagrs
                self.ip = addr
            elif opcode == instruction("RET"):
                self.ip = self.callstack[self.callsp].returnip
                self.callsp -=1
            elif opcode == instruction("PRINT"):
                arg = self.code[self.ip]
                self.ip += 1
                value = self.stack[self.sp - arg + 1:self.sp]
                self.sp -= arg
                print("".join(chr(x) for x in value), end="")
            elif opcode == instruction("HALT"):
                self.h = 0
            else:
                raise BaseException("opcode " + str(opcode)+ " is not implemented")
            
            if(self.debug):self._trace_stack()

        if(self.debug):
            self._globals_dumps()
        return self.h