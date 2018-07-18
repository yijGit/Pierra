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

    def isEmpty(self):
        return self.stack.isEmpty()

    '''
    def naming(self, names: dict):
        title = '' + str(self.length)
        string = ''
        char_array = names.get(title)
        for i in range(0, 26):
            for j in range(0, 26):
                for z in range(0, 26):
                    chars= [97 + i, 97 + j, 97 + z]
                    for k in range(0, 3):
                        a = chr(chars[k])
                        string += a
                    if char_array[i * 26 * 26 + j * 26 + z] == string:
                        names[title] = string
                        title += string
                        break
    '''