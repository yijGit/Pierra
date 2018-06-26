

"""
A simple VM interpreter.
Code from the post at http://csl.name/post/vm/
This version should work on both Python 2 and 3.
"""

from __future__ import *
from collections import deque
from io import *
import sys
import tokenize


def get_input(*args, **kw):
    """Read a string from standard input."""
    if sys.version[0] == "2":
        return input(*args, **kw)
    else:
        return input(*args, **kw)


class Stack(deque):
    push = deque.append

    def top(self):
        return self[-1]


class Machine:
    def __init__(self, code):
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
            "17": self.iffl, # if flag == 1
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
            self.push(op) # push numbers on stack
        elif isinstance(op, str) and op[0]==op[-1]=='"':
            self.push(op[1:-1]) # push quoted strings on stack
        else:
            raise RuntimeError("Unknown opcode: '%s'" % op)

    # OPERATIONS FOLLOW:

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
        pass

    def ifz(self):
        if(CX == 0):
            pass
        else:
            jmp(instruction_pointer + 2)

    def iffl(self):
        if(flag == 1):
            pass
        else:
            jmp(instruction_pointer + 2)

    def jmp(self):
        addr = instruction_pointer + 2
        if isinstance(addr, int) and 0 <= addr < len(self.code):
            self.instruction_pointer = addr
        else:
            raise RuntimeError("JMP address must be a valid integer.")
    def jmpb(self):
        pass

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



def parse(text):
    # Note that the tokenizer module is intended for parsing Python source
    # code, so if you're going to expand on the parser, you may have to use
    # another tokenizer.

    if sys.version[0] == "2":
        stream = StringIO(unicode(text))
    else:
        stream = StringIO(text)

    tokens = tokenize.generate_tokens(stream.readline)

    for toknum, tokval, _, _, _ in tokens:
        if toknum == tokenize.NUMBER:
            yield int(tokval)
        elif toknum in [tokenize.OP, tokenize.STRING, tokenize.NAME]:
            yield tokval
        elif toknum == tokenize.ENDMARKER:
            break
        else:
            raise RuntimeError("Unknown token %s: '%s'" %
                    (tokenize.tok_name[toknum], tokval))


def repl():
    print('Hit CTRL+D or type "exit" to quit.')

    while True:
        try:
            source = get_input("> ")
            code = list(parse(source))
            code = constant_fold(code)
            Machine(code).run()
        except (RuntimeError, IndexError) as e:
            print("IndexError: %s" % e)
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt")

def examples():
    print("** Program 1: Runs the code for `print((2+3)*4)`")
    Machine([2, 3, "+", 4, "*", "println"]).run()

    print("\n** Program 2: Ask for numbers, computes sum and product.")
    Machine([
        '"Enter a number: "', "print", "read", "cast_int",
        '"Enter another number: "', "print", "read", "cast_int",
        "over", "over",
        '"Their sum is: "', "print", "+", "println",
        '"Their product is: "', "print", "*", "println"
    ]).run()

    print("\n** Program 3: Shows branching and looping (use CTRL+D to exit).")
    Machine([
        '"Enter a number: "', "print", "read", "cast_int",
        '"The number "', "print", "dup", "print", '" is "', "print",
        2, "%", 0, "==", '"even."', '"odd."', "if", "println",
        0, "jmp" # loop forever!
    ]).run()


if __name__ == "__main__":
    try:
        if len(sys.argv) > 1:
            cmd = sys.argv[1]
            if cmd == "repl":
                repl()
            elif cmd == "test":
                test()
                examples()
            else:
                print("Commands: repl, test")
        else:
            repl()
    except EOFError:
        print("")
