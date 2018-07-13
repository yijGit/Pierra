"""
A sample CPU class for use in every organism
"""

from LocMem import *

class CPU():
    def __init__(self, code, RAM):

        # the instruction set that the CPU must now perform
        self.code = code

        # the RAM inside the soup
        self.RAM = RAM

        self.daughter = None

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

        # the registers and the data stack
        self.mem = CPUMem()

        # the instruction pointer that indicates where we are in the instruction set
        self.ip = 0

        # TODO: Figure out if flag is in memory or in the CPU
        self.flag = 0

    # the fetch-decode-execute loop of the CPU
    def run(self) -> None:
        for self.ip in range(len(self.code)):
            opcode = self.fetch()
            self.decode(opcode)
        self.ip = 0

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
        pass

    def get(self):
        self.mem.dx = int(input())

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

    def jmp(self):
        # jmp to template, or if no template jmp back to address in ax
        template = self.temp()
        if self.test():
            self.ip = self.compl(template, 1)
        else:
            self.ip = self.mem.ax

    def jmpb(self):
        # jmp back to template, or if no template jmp back to address in ax
        pass

    def call(self):
        # push IP + 1 onto the stack; if template, jmp to complementary temp1
        self.mem.push(self.code[self.ip + 1])

    def adr(self):
        # search outward for template
        self.mem.ax = address
        self.mem.dx = size
        self.mem.cx = offset


    def adrb(self):
        pass

    def adrf(self):
        pass

    def mal(self, num_cells):
        d_code = open("creature" + num_cells + ".py", "wb")
        for i in range(len(self.code)):
            d_code.write(self.code[i] + '\n')
        d_cpu = CPU(d_code)
        d_mem = CPUMem()
        self.daughter


    def divide(self):
        self.instruction_pointer += self.mem.cx
        self.daughter.mem.ax = self.mem.ax
        self.daughter.mem.bx = self.mem.bx
        self.daughter.mem.cx = self.mem.cx
        self.daughter.mem.dx = self.mem.dx




    def temp(self):
        template = self.code[2 * self.instruction_pointer + 2: 2 * self.instruction_pointer + 11]
        return template

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

    def print(self):
        print(self.mem.top())

codes = [1, 0, 15, 15, 15, 15, 7, 32]
main = CPU(codes)
main.run()
