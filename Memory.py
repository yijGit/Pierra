class G_Memory:
    def __init__(self):
        self.RAM = [0] * 60000 # soup
        self.library = {'80aaa': 2} # genotype: index

    def get(self, offset, value):
        size = len(value)
        return self.RAM[offset: offset + size]
    def set(self, offset, value):
        size = len(value)
        self.RAM[offset: offset + size] = value
    def fill(self, value):
        for i in range(len(self.RAM)):
            self.RAM[i] = value

class L_Memory:
    def __init__(self):
        ax = 0  # address register
        bx = 0  # ditto
        cx = 0  # numeric register
        dx = 0  # ditto
        fl = 0  # error conditions
        sp = 0  # stack pointer
        st = [0] * 10  # ten-word stack
        ip = 0  # instruction pointer
