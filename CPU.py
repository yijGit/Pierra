"""
A sample CPU class for use in every organism
"""

from LocMem import *
from Memory import G_Memory
from Organism import Organism
from OS import operating_system
import random

class CPU:
    def __init__(self, os: operating_system):

        # the instruction set that the CPU must now perform

        self.os = os

        self.accessory = os.soup.accessory

        self.property = os.soup.property

        # the RAM inside the soup
        self.RAM = os.soup.ram

        self.countdown = 0

        # the registers and the data stack
        self.mem = CPUMem()

        # the complete list of instructions with the corresponding opcodes
        self.dispatch_map = {
            0x00: self.nop0,
            0x01: self.nop1,
            0x02: self.movdi,
            0x03: self.movid,
            0x04: self.movii,
            0x05: self.pushax,
            0x06: self.pushbx,
            0x07: self.pushcx,
            0x08: self.pushdx,
            0x09: self.popax,
            0x0a: self.popbx,
            0x0b: self.popcx,
            0x0c: self.popdx,
            0x0d: self.put,
            0x0e: self.get,
            0x0f: self.inc,
            0x10: self.dec,
            0x11: self.add,
            0x12: self.sub,
            0x13: self.zero,
            0x14: self.not0,
            0x15: self.shl,
            0x16: self.ifz,
            0x17: self.iffl,  # if flag == 1
            0x18: self.jmp,
            0x19: self.jmpb,
            0x1a: self.call,
            0x1b: self.adr,
            0x1c: self.adrb,
            0x1d: self.adrf,
            0x1e: self.mal,
            0x1f: self.divide,
            0x20: self.print
        }

        # the instruction pointer that indicates where we are in the instruction set
        self.ip = 0

        # TODO: Figure out if flag is in memory or in the CPU
        self.flag = 0

        # the daughter
        self.daughter = None

    # the fetch-decode-execute loop of the CPU
    def run(self) -> None:
        while self.organism.countdown > 0:
            opcode = self.fetch()
            self.decode(opcode)
            self.organism.countdown -= 1
            self.ip += 1
        self.os.slicer_rotate()

    def fetch(self) -> int:
        op = self.code[self.ip]
        return op

    def decode(self, opcode) -> None:
        if opcode in self.dispatch_map:
            self.dispatch_map.get(opcode, lambda: 'Not in dispatch map')()
        # TODO: figure out what to do if NOT in dispatch_map

    # no operations
    def nop0(self):
        pass

    def nop1(self):
        pass

    # memory movement
    def movdi(self):
        self.RAM[self.mem.ax + self.mem.cx] = self.mem.bx

    def movid(self):
        self.mem.ax = self.RAM[self.mem.bx + self.mem.cx]

    def movii(self):
        self.RAM[self.mem.ax + self.mem.cx] = self.RAM[self.mem.bx + self.mem.cx]

    def pushax(self):
        self.mem.push(self.mem.ax)
        self.mem.ax = 0

    def pushbx(self):
        self.mem.push(self.mem.bx)
        self.mem.bx = 0

    def pushcx(self):
        self.mem.push(self.mem.cx)
        self.mem.cx = 0

    def pushdx(self):
        self.mem.push(self.mem.dx)
        self.mem.dx = 0

    def popax(self):
        self.mem.ax = self.mem.pop()

    def popbx(self):
        self.mem.bx = self.mem.pop()

    def popcx(self):
        self.mem.cx = self.mem.pop()

    def popdx(self):
        self.mem.dx = self.mem.pop()

    def put(self):
        template = self.__read()
        PutLimit = 100
        if self.__test(template):
            compl = self.__compl(template)
            for i in range(0, PutLimit):
                if RAM[self.ip + self.start + i] == 
        else:
            if self.property.get(self.mem.cx) == self.name:
                other = self.accessory.get(self.property.get(self.mem.cx))
                other.mem.input_buffer = self.mem.dx


    def get(self):
        self.mem.dx = self.mem.input_buffer

    # calculations
    def inc(self):
        self.mem.cx += 1

    def dec(self):
        self.mem.cx -= 1

    def add(self):
        self.mem.cx += self.mem.dx

    def sub(self):
        self.mem.cx -= self.mem.dx

    def zero(self):
        self.mem.cx = 0

    def not0(self):
        self.mem.cx = self.mem.cx ^ 1

    def shl(self):
        self.mem.cx = self.mem.cx << 1

    # instruction pointer manipulation
    def ifz(self) -> None:
        if self.mem.cx == 0:
            return
        else:
            self.ip += 1

    def iffl(self) -> None:
        if self.flag == 1:
            return
        else:
            self.ip += 1

    def jmp(self) -> None:
        # jmp to template, or if no template jmp back to address in ax
        template = self.__read()
        if self.__test(template):
            temp = self.ip + 1
            complement = self.__compl(template)
            # TODO: Add a case if nothing is found
            while temp < len(code) - 3:
                if code[temp: temp + 4] == complement:
                    self.ip = temp + 4
                    break
                temp += 1
        else:
            self.ip = self.mem.ax

    def jmpb(self):
        # jmp back to template, or if no template jmp back to address in ax
        template = self.__read()
        if self.__test(template):
            temp = self.ip
            complement = self.__compl(template)
            # TODO: Add a case if nothing is found
            while temp - 3 > 0:
                if code[temp - 4: temp] == complement:
                    self.ip = temp + 1
                    break
                temp -= 1
        else:
            self.ip = self.mem.ax

    """
        template = self.temp()
        if self.test():
            self.instruction_pointer = self.compl(template, 0)
        else:
            self.instruction_pointer = self.AX
    """

    def __test(self, template) -> bool:
        for i in range(len(template)):
            if template[i] != 0x01 and template[i] != 0x00:
                return False
        return True

    def __read(self) -> bytearray:
        template = bytearray()
        for i in range(1, 5):
            template.append(self.code[self.ip + i])
        return template

    def __compl(self, template) -> bytearray:
        complement = bytearray()
        for i in range(len(template)):
            complement.append(template[i] ^ 1)
        return complement

    def call(self):
        # push IP + 1 onto the stack; if template, jmp to complementary temp1
        self.mem.push(self.ip + 1)
        if template:
            jmp(temp1)

    def adr(self):
        # search outward for template
        self.mem.ax = address
        self.mem.dx = size
        self.mem.cx = offset


    def adrb(self):
        pass

    def adrf(self):
        pass

    def mal(self):
        size = self.mem.cx
        d_start = self.mem.ax
        m_start = self.mem.bx
        for i in range(0, size):
            property{d_start + i : self.mem.name}


    def divide(self):
        self.instruction_pointer += self.mem.cx
        self.daughter.mem.ax = self.mem.ax
        self.daughter.mem.bx = self.mem.bx
        self.daughter.mem.cx = self.mem.cx
        self.daughter.mem.dx = self.mem.dx





    def print(self):
        print('AX = ' + str(self.mem.ax))
        print('BX = ' + str(self.mem.bx))
        print('CX = ' + str(self.mem.cx))
        print('DX = ' + str(self.mem.dx))

fram = bytearray()

fram.append(0x01)
fram.append(0x00)
fram.append(0x0f)
fram.append(0x0f)
fram.append(0x0f)
fram.append(0x0f)
fram.append(0x20)
codes = [1, 0, 15, 15, 7, 12, 15, 15, 7, 9, 32, 16, 16, 16, 32]
RAM = G_Memory()
main = CPU(fram, RAM)
main.run()
