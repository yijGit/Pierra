class Organism:
    def __init__(self, code, CPU):
        self.error_fault = 0
        self.code = code
        self.CPU = CPU
        self.ax = 0  # address register
        self.bx = 0  # ditto
        self.cx = 0  # numeric register
        self.dx = 0  # ditto
        self.fl = 0  # error conditions
        self.sp = 0  # stack pointer
        self.st = [0] * 10  # ten-word stack
        self.ip = 0  # instruction pointer
        self.mother = 'original'

    def isMother(self) -> bool:
        return True
    def isDaughter(self) -> bool:
        return False
    def geneology(self) -> str:
        return "HALP"

