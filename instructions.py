from collections import deque

class Stack(deque):
    push = deque.append
    def top(self):
        return self[-1]

class Machine:
    def __init__(self, code):
        self.data_stack = Stack()
        self.instruction_stack = Stack()
        self.instruction_pointer = 0
        self.stack_pointer = 0
        self.base_pointer = 0
        self.AX = None
        self.BX = None
        self.CX = None
        self.DX = None
        self.dictionary = {




        }

    def nop0:
        pass

    def nop1:
        pass

    def movdi:
        self.stack.