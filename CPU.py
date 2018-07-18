"""
A sample CPU class for use in every organism
"""

from LocMem import *
from Memory import G_Memory
from OS import operating_system
import random

class CPU:
    def __init__(self, os: operating_system):

        # the instruction set that the CPU must now perform

        self.os = os

        self.accessory = os.soup.accessory

        self.property = os.soup.property

        # the RAM inside the soup
        self.RAM = os.soup.RAM

        # the registers and the data stack
        self.mem = CPUMem()

        self.countdown = 0

        self.name = self.mem.naming(os.soup.names)

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

        # TODO: Figure out if flag is in memory or in the CPU
        self.flag = 0
        self.random = random.random() * (2500 - 1000) + 1000

    # the fetch-decode-execute loop of the CPU
    def run(self) -> None:
        while self.countdown > 0:
            opcode = self.fetch()
            #print('ip before executing = ' + str(self.mem.ip))
            #print('ip: ' + str(self.mem.ip) + ' / opcode = ' + str(hex(opcode)))
            self.decode(opcode)
            '''
            print('     self.mem.ax = ' + str(self.mem.ax))
            print('     self.mem.bx = ' + str(self.mem.bx))
            print('     self.mem.cx = ' + str(self.mem.cx))
            print('     self.mem.dx = ' + str(self.mem.dx))
            
            if not self.mem.isEmpty():
                print('     top of stack = ' + str(self.mem.top()))
                '''
            self.countdown -= 1
            self.mem.ip += 1
            self.os.soup.total_instructions += 1
            if self.os.soup.total_instructions == 10000:
                self.os.cosmic_ray()
                #for i in range(len(self.RAM)):
                    #print("index: "+ str(i) +" and opcode: " + str(hex(self.RAM[i])))

    def fetch(self) -> int:
        op = self.RAM[self.mem.ip]
        return op

    def decode(self, opcode) -> None:
        if opcode in self.dispatch_map:
            self.dispatch_map.get(opcode, lambda: 'Not in dispatch map')()
        # TODO: figure out what to do if NOT in dispatch_map

    def updateCountdown(self, cd):
        self.countdown = cd

    # no operations
    def nop0(self):
        pass

    def nop1(self):
        pass

    # memory movement
    def movdi(self):
        if self.property.get(self.mem.ax + self.mem.cx) == self.name:
            self.RAM[self.mem.ax + self.mem.cx] = self.mem.bx
        self.movement()

    def movid(self):
        self.mem.ax = self.RAM[self.mem.bx + self.mem.cx]

    def movii(self):
        if self.property.get(self.mem.ax + self.mem.cx) == self.name:
        #print('AX = ' + str(self.mem.ax))
        #print('BX = ' + str(self.mem.bx))
        #print('CX = ' + str(self.mem.cx))
        #AXCX = self.mem.ax + self.mem.cx
        #BXCX = self.mem.bx + self.mem.cx
        #print(str(BXCX) + ' to ' + str(AXCX))
            self.RAM[self.mem.ax + self.mem.cx + 1] = self.RAM[self.mem.bx + self.mem.cx]
            self.movement()

    def movement(self):
        self.mem.movement += 1
        if self.mem.movement == self.random:
            self.os.mutation(self.mem.ax + self.mem.cx)
            self.random = random.random * (2500 - 1000) + 1000

    def pushax(self):
        self.mem.push(self.mem.ax)

    def pushbx(self):
        self.mem.push(self.mem.bx)

    def pushcx(self):
        self.mem.push(self.mem.cx)

    def pushdx(self):
        self.mem.push(self.mem.dx)

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
                forward = self.mem.ip + self.mem.start + i
                backward = self.mem.ip + self.mem.start - i
                if self.RAM[forward: forward + 4] == compl:
                    other = self.accessory.get(self.property.get(forward))
                    other.mem.input_buffer = self.mem.dx
                if self.RAM[backward - 4: backward] == compl:
                    other = self.accessory.get(self.property.get(backward))
                    other.mem.input_buffer = self.mem.dx
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
            self.mem.ip += 1

    def iffl(self) -> None:
        if self.flag == 1:
            return
        else:
            self.mem.ip += 1

    def jmp(self) -> None:
        template = self.__read()
        jump_limit = 100
        if self.__test(template):
            self.mem.ip += 1
            complement = self.__compl(template)
            while jump_limit > 0:
                pointer = self.mem.ip
                if self.RAM[pointer: pointer + len(template)] == complement:
                    self.mem.ip = pointer + len(template) - 1
                    break
                self.mem.ip += 1
                jump_limit -= 1
        else:
            self.mem.ip = self.mem.ax

    def jmpb(self):
        template = self.__read()
        jump_limit = 100
        if self.__test(template):
            complement = self.__compl(template)
            while jump_limit > 0:
                pointer = self.mem.ip
                if self.RAM[pointer - len(template): pointer] == complement:
                    self.mem.ip = pointer - 1
                    break
                self.mem.ip -= 1
                jump_limit -= 1
        else:
            self.mem.ip = self.mem.ax

    def __read(self) -> bytearray:
        template = bytearray()
        pointer = self.mem.ip + 1
        opcode = self.RAM[pointer]
        while opcode == 0x00 or opcode == 0x01:
            template.append(opcode)
            pointer += 1
            opcode = self.RAM[pointer]
        return template

    def __test(self, template) -> bool:
        return len(template) != 0

    def __compl(self, template) -> bytearray:
        complement = bytearray()
        for i in range(len(template)):
            complement.append(template[i] ^ 1)
        return complement

    def call(self):
        # push IP + 1 onto the stack; if template, jmp to complementary temp1
        self.mem.push(self.mem.ip + 1)
        self.jmp()

    def adr(self):
        #TODO: Figure out offset without defaulting to zero
        #TODO: Figure out what happens if there is no template
        self.adrb()
        tempax = self.mem.ax
        tempdx = self.mem.dx
        self.adrf()
        tempax2 = self.mem.ax
        tempdx2 = self.mem.dx
        if tempax < tempax2:
            self.mem.ax = tempax
        if tempdx < tempdx2:
            self.mem.dx = tempdx

    def adrb(self):
        self.mem.cx = 0
        template = self.__read()
        self.mem.dx = len(template)
        adr_limit = 100
        pointer = self.mem.ip
        if self.__test(template):
            complement = self.__compl(template)
            while adr_limit > 0:
                if self.RAM[pointer - len(template): pointer] == complement:
                    self.mem.ax = pointer
                    self.mem.ip += len(template)
                    break
                pointer -= 1
                adr_limit -= 1
        else:
            pass

    def adrf(self):
        self.mem.cx = 0
        template = self.__read()
        self.mem.dx = len(template)
        adr_limit = 100
        pointer = self.mem.ip
        if self.__test(template):
            pointer += 1
            complement = self.__compl(template)
            while adr_limit > 0:
                if self.RAM[pointer: pointer + len(template)] == complement:
                    self.mem.ax = pointer + len(template)
                    self.mem.ip += len(template)
                    break
                pointer += 1
                adr_limit -= 1
        else:
            pass

    def mal(self):
        size = self.mem.cx
        d_start = self.mem.ax
        for i in range(0, size):
            self.property[d_start + i] = self.name

    def divide(self):
        daughter = CPU(self.os)
        daughter.mem.ip += self.mem.cx
        daughter.mem.ax = self.mem.ax
        daughter.mem.bx = self.mem.bx
        daughter.mem.cx = self.mem.cx
        daughter.mem.dx = self.mem.dx
        daughter.mem.start = self.mem.dx + self.mem.cx
        daughter.mem.length = self.mem.cx
        daughter.mem.end = daughter.mem.start + daughter.mem.length
        daughter.mem.naming(self.RAM, daughter.mem.length)
        print(daughter.mem.name)
        for i in range(daughter.mem.start, daughter.mem.end + 1):
            self.property[i] = daughter.mem.name
        self.os.reapUpdate(daughter.mem.name)
        self.os.soup.accessory[daughter.mem.name] = daughter
        self.mem.ip = daughter.mem.start
        self.os.slicer_increase(self, daughter)
        self.countdown = 0

    def print(self):
        print('AX = ' + str(self.mem.ax))
        print('BX = ' + str(self.mem.bx))
        print('CX = ' + str(self.mem.cx))
        print('DX = ' + str(self.mem.dx))

'''
codes = [0x1, 0x1, 0x1, 0x1, 0x13, 0x1c, 0x00, 0x00, 0x00, 0x00, 0x05, 0x0b, 0x12, 0x07, 0x13, 0x1d, 0x00, 0x00, 0x00, 0x01, 0x05, 0x0b, 0x0f, 0x0c, 0x12, 0x01, 0x01, 0x00, 0x01,
         0x1e, 0x1a, 0x00, 0x00, 0x01, 0x01, 0x1f, 0x19, 0x00, 0x00, 0x01, 0x00, 0x16, 0x01, 0x01, 0x00, 0x00, 0x07, 0x08, 0x08, 0x0a, 0x01, 0x00, 0x01, 0x00, 0x10, 0x04,
         0x16, 0x18, 0x00, 0x01, 0x00, 0x00, 0x19, 0x00, 0x01, 0x00, 0x01, 0x16, 0x01, 0x00, 0x01, 0x01, 0x0c, 0x0b, 0x09, 0x18, 0x16, 0x01, 0x01, 0x01, 0x00, 0x16]
memory = G_Memory()
print(len(codes))
for i in range(len(codes)):
    memory.RAM[i] = codes[i]

print('BEFORE RUNNING: MOTHER -------------')
for i in range(len(codes)):
    print(hex(memory.RAM[i]))

OS = operating_system(memory)
main = CPU(OS)
main.run()

print('AFTER RUNNING: MOTHER -----------------------')
for i in range(len(codes)):
    print(hex(memory.RAM[i]))
print('SECOND ----------------------')
for i in range(len(codes), len(codes) * 2):
    print(hex(memory.RAM[i]))
    '''

