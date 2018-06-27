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
        if op in dispatch_map:
            dispatch_map[op]()
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

    def get(self):
        self.DX = input()

    def inc(self):
        CX += 1
        self.push(CX)

    def dec(self):
        CX -= 1
        self.push(CX)

    def add(self):
        CX += DX
        self.push(CX)

    def minus(self):
        CX -= DX
        self.push(CX)

    def zero(self):
        CX = 0
        self.push(CX)

    def not0(self):
        binary = bin(CX)[2:]
        binary = binary.charAt(0) + (binary.charAt(1) & f)  # 32 bit representation
        self.push(binary)

    def shl(self):
        binary = bin(CX)[2:]
        binary = binary << 2
        self.push(binary)

    def ifz(self):
        if (CX == 0):
            pass
        else:
            jmp(instruction_pointer + 2)  # fix!!!!!

    def iffl(self):
        if (flag == 1):
            pass
        else:
            jmp(instruction_pointer + 2)  # fix!!!!!

    def jmp(self):  # read next four noop instructions: Assume Template
        template = code[2 * instruction_pointer + 1: 2 * instruction_pointer + 10]  # Trying to find template
        complement = complement = compl(template)
        for i in range(len(code))
            if complement == code[i:i + 9]:
                instruction_pointer = (i + 8) / 2 + 1
        break

    def jmpb(self):  # Read Last four noop instructions: Assume Template
        template = code[2 * instruction_pointer + 1: 2 * instruction_pointer + 10]  # Trying to find template
        complement = compl(template)
        for i in range(len(code))
            if complememnt == code i:i + 9

            def __compl(self, template):

    complement = ""
    for i in range(len(template)):
        if i % 2 != 0:
            if template.charAt(i) == 0:
                complement + "1"
            else
                complement + "0"
        else
            complement + "0"
    return complement


def call(self):
    pass


def mod(self):
    last = self.pop()
    self.push(self.pop() % last)


def read(self):
    self.push(get_input())


def eq(self):
    self.push(self.pop() == self.pop())


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