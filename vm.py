"""
A simple VM interpreter.
Code from the post at http://csl.name/post/vm/
This version should work on both Python 2 and 3.
"""

from collections import deque
import sys
import os
import random

class Stack(deque):
    push = deque.append

    def top(self):
        return self[-1]
class Machine:
    def __init__(self, code):
        self.code = code
        self.dispatch_map = {
            "00": self.nop0,
            "01": self.nop1,
            "02": self.movdi,
            "03": self.movid,
            "04": self.movii,
            "05": self.pushax,
            "06": self.pushbx,
            "07": self.pushcx,
            "08": self.pushdx,
            "09": self.popax,
            "0a": self.popbx,
            "0b": self.popcx,
            "0c": self.popdx,
            "0d": self.put,
            "0e": self.get,
            "0f": self.inc,
            "10": self.dec,
            "11": self.add,
            "12": self.sub,
            "13": self.zero,
            "14": self.not0,
            "15": self.shl,
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
        if(self.test()):
            template = self.temp()
            for cell in self.soup:
                cell.get() # genotype
        else:
            pass


    def get(self):
        self.DX = input()

    def inc(self):
        if random.random < .95:
            self.CX += 1
        else:
            if random.random< .5:
                self.CX += 0
            else:
                self.CX += 2

        self.push(self.CX)

    def dec(self):
        if random.random < .95:
            self.CX -= 1
        else:
            if random.random < .5:
                self.CX -= 0
            else:
                self.CX -= 2
        self.push(self.CX)

    def add(self):
        self.CX += self.DX
        self.push(self.CX)

    def sub(self):
        self.CX -= self.DX
        self.push(self.CX)

    def zero(self):
        self.CX = 0
        self.push(self.CX)

    def not0(self):
        binary = bin(self.CX)[2:]
        binary = binary.charAt(0) + (binary.charAt(1))  # 32 bit representation
        self.push(binary)

    def shl(self):
        binary = bin(self.CX)[2:]
        binary = binary << 1
        self.CX = binary
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
        template = self.temp()
        if self.test():
            self.instruction_pointer = self.compl(template, 1)
        else:
            self.instruction_pointer = self.AX


    def jmpb(self):  # Read Last four noop instructions: Assume Template
        template = self.temp()
        if self.test():
            self.instruction_pointer = self.compl(template, 0)
        else:
            self.instruction_pointer = self.AX


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
    def test(self):
        template = self.temp()
        for i in range(len(template)):
            if i % 2 != 0:
                if i is not 0 or 1:
                    return False
                else:
                    return True
            else:
                if i is not 0:
                    return False
                else:
                    return True
    def temp(self):
        template = self.code[2 * self.instruction_pointer + 2: 2 * self.instruction_pointer + 11]
        return  template

    def call(self):
        self.push(self.instruction_pointer + 1)
        template = self.code[2 * self.instruction_pointer + 1: 2 * self.instruction_pointer + 10]
        flag = self.test(template)
        if flag:
            self.jmp()

    def adr(self, RAM):
        pass

    def adrb(self):
        pass

    def adrf(self):
        pass

    def mal(self):
        pass

    def divide(self, num_cells):
        self.instruction_pointer += self.CX
        daughter = open("creature"+num_cells+".py","wb")
        daughter.write(bytes("Machine[" + self.code + "]",'UTF-8'))

    def print(self):
        pass

class CPU:  # computations must be probalistic
    def __init__(self):
        ax = 0  # address register
        bx = 0  # ditto
        cx = 0  # numeric register
        dx = 0  # ditto
        fl = 0  # error conditions
        sp = 0  # stack pointer
        st = [0] * 10  # ten-word stack
        ip = 0  # instruction pointer

    def life(self):
        while (instr_exec_c < alive):
            self.time_slice(this_slice)
            incr_slice_queue()
            while(free_mem_current < free_mem_prop * soup_size)
                reaper()

    def time_slice(self, ci):
        Pcells ce  # pointer to array of cell structures
        i = ''
        di, j, size_slice = 0
        ce = cells + ci
        for j in range(len(size_slice)):
            i = fetch(ce ->c.ip)
            di = decode(i)
            execute(di, ci)
            increment_ip(di, ce)
            system_work()

