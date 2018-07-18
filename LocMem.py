from collections import deque

class Stack(deque):
    push = deque.append

    def top(self):
        return self[-1]

    def isEmpty(self):
        return len(self) == 0

class CPUMem:
    def __init__(self):
        # stack
        self.stack = Stack()

        # registers
        self.ax = 0
        self.bx = 0
        self.cx = 0
        self.dx = 0

        # other miscellaneous data
        self.error_faults = 0
        self.start = 0
        self.end = 0
        self.movement = 0
        self.name = ''
        self.length = 0

        # stack and instruction pointer
        self.sp = 0
        self.input_buffer = None
        self.total_moved = 0
        self.ip = self.start



    # methods that assist in changing the state of the data stack
    def pop(self):
        return self.stack.pop()

    def push(self, value):
        self.stack.push(value)

    def top(self):
        return self.stack.top()

    def naming(self, names: dict):
        title = self.length
        if title in names:
            num_names = names[title]
        else:
            num_names = 0
            names[title] = 0
        first = int(num_names / (26 * 26)) + 97
        second = int((num_names - (first - 97) * 26 * 26) / 26) + 97
        third = (num_names - (second - 97) * 26 - (first - 97) * 26 * 26) + 97
        fir = chr(first)
        sec = chr(second)
        thir = chr(third)
        string = ''.join([fir, sec, thir])
        names[title] += 1
        print("lines:" +str(title) + " #: " + str(names[title]) + " string: " + string)
        self.name = str(title) + string

    def isEmpty(self):
        return self.stack.isEmpty()