"""
A simple VM interpreter.
Code from the post at http://csl.name/post/vm/
This version should work on both Python 2 and 3.
"""

from collections import deque


class Stack(deque):
    push = deque.append

    def top(self):
        return self[-1]


class Machine:
    def __init__(self, code):
        self.RAM = [60000]
        self.data_stack = Stack()
        self.return_stack = Stack()
        self.instruction_pointer = 0
        self.stack_pointer = 0
        self.base_pointer = 0
        self.code = code
        self.flag = 0
        self.AX = None
        self.BX = None
        self.CX = None
        self.DX = None
        self.flag = None
        self.dispatch_map = {
            "00": self.nop0,
            "01": self.nop1,
            "02": self.movdi,
            "03": self.movid,
            "04": self.movii,
            "05": self.pushax,
            "06": self.push,
            "07": self.pushC,
            "08": self.pushD,
            "09": self.popA,
            "0a": self.popB,
            "0b": self.popC,
            "0c": self.popD,
            "0d": self.put,
            "0e": self.get,
            "0f": self.inc,
            "10": self.dec,
            "11": self.add,
            "12": self.sub,
            "13": self.zero,
            "14": self.NOT,
            "15": self.shift,
            "16": self.ifz,
            "17": self.iffl,  # if flag == 1
            "18": self.jmp,
            "19": self.jmpb,
            "1a": self.call,
            "1b": self.adr,
            "1c": self.adrb,
            "1d": self.adrf,
            "1e": self.mal,
            "1f": self.divide}

    def pop(self):
        return self.data_stack.pop()

    def push(self, value):
        self.data_stack.push(value)

    def top(self):
        return self.data_stack.top()

    def run(self):
        while self.instruction_pointer < len(self.code):
            opcode = self.code[self.instruction_pointer]
            self.instruction_pointer += 1
            self.dispatch(opcode)

    def dispatch(self, op):
        if op in self.dispatch_map:
            self.dispatch_map[op]()
        elif isinstance(op, int):
            self.push(op)  # push numbers on stack
        elif isinstance(op, str) and op[0] == op[-1] == '"':
            self.push(op[1:-1])  # push quoted strings on stack
        else:
            raise RuntimeError("Unknown opcode: '%s'" % op)

    # OPERATIONS FOLLOW:
    def nop0(self):
        pass

    def nop1(self):
        pass

    def movdi(self):
        self.ram[self.AX + self.BX] = self.BX
        self.BX = None

    def movid(self):
        self.AX = self.ram[self.BX + self.CX]
        self.ram[self.BX + self.CX] = None

    def movii(self):
        self.ram[self.AX + self.CX] = self.ram[self.BX + self.CX]
        self.ram[self.BX + self.CX] = None

    def pushax(self):
        self.data_stack.push(self.AX)
        self.AX = None

    def pushbx(self):
        self.data_stack.push(self.BX)
        self.BX = None

    def pushcx(self):
        self.data_stack.push(self.CX)
        self.CX = None

    def pushdx(self):
        self.data_stack.push(self.DX)
        self.DX = None

    def popax(self):
        self.AX = self.data_stack.pop()

    def popbx(self):
        self.BX = self.data_stack.pop()

    def popcx(self):
        self.CX = self.data_stack.pop()

    def popdx(self):
        self.DX = self.data_stack.pop()

    def put(self):
        pass

    def get(self):
        self.DX = input()

    def inc(self):
        self.CX += 1
        self.push(self.CX)

    def dec(self):
        self.CX -= 1
        self.push(self.CX)

    def add(self):
        self.CX += self.DX
        self.push(self.CX)

    def minus(self):
        self.CX -= self.DX
        self.push(self.CX)

    def zero(self):
        self.CX = 0
        self.push(self.CX)

    def not0(self):
        binary = hex(self.CX)[2:]
        binary = binary.charAt(0) + (binary.charAt(1) & hex.f)  # 32 bit representation
        self.push(binary)

    def shl(self):
        binary = hex(self.CX)[2:]
        binary = binary << 1
        self.push(binary)

    def ifz(self):
        if (self.CX == 0):
            pass
        else:
            self.instruction_pointer += 1

    def iffl(self):
        if (self.flag == 1):
            pass
        else:
            self.instruction_pointer += 1

    def jmp(self):  # read next four noop instructions: Assume Template
        template = self.code[2 * self.instruction_pointer + 1: 2 * self.instruction_pointer + 10]  # Trying to find template
        self.instruction_pointer = self.compl(template, 1)


    def jmpb(self):  # Read Last four noop instructions: Assume Template
        template = self.code[2 * self.instruction_pointer + 1: 2 * self.instruction_pointer + 10]  # Trying to find template
        self.instruction_pointer = self.compl(template, 0)


    def compl(self, template, dir):
        complement = ""
        for i in range(len(template)):
            if i % 2 != 0:
                if template.charAt(i) == 0:
                    complement + "1"
                else:
                    complement + "0"
            else:
                complement + "0"
        for i in range(len(self.code)):
            if complement == self.code[i:i + 9]:
                if dir == 1:
                    self.instruction_pointer = (i + 8) / 2 + 1
                elif dir == 0:
                    self.instruction_pointer = i / 2
                else:
                    NotImplementedError("BAD")
        return self.instruction_pointer
    def test(self, template):
        pass

def call(self):
    self.push(self.instruction_pointer + 1)
    pass


def if_stmt(self):
    false_clause = self.pop()
    true_clause = self.pop()
    test = self.pop()
    self.push(true_clause if test else false_clause)


def jmp(self):
    addr = self.pop()
    if isinstance(addr, int) and 0 <= addr < len(self.code):
        self.instruction_pointer = addr
    else:
        raise RuntimeError("JMP address must be a valid integer.")