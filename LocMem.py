from collections import deque

class Stack(deque):
    push = deque.append

    def top(self):
        return self[-1]

class CPUMem:
    def __init__(self):
        # stack
        self.stack = Stack()

        # registers
        self.ax = 0
        self.bx = 0
        self.cx = 0
        self.dx = 0

        # stack and instruction pointer
        self.sp = 0
        self.input_buffer = None
        self.total_moved = 0

        # other miscellaneous data
        self.error_faults = 0
        self.start = 0
        self.end = 0
        self.movement = 0
        self.name = ''
        self.length = 0

    # methods that assist in changing the state of the data stack
    def pop(self):
        return self.stack.pop()

    def push(self, value):
        self.stack.push(value)

    def top(self):
        return self.stack.top()

    def name(self):
        pass

