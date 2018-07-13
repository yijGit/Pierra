from CPU import CPU
from Memory import G_Memory
from OS import operating_system
from LocMem import CPUMem

class Organism:

    def __init__(self, code: bytearray, processor: CPU, Local: CPUMem):
        self.error_fault = 0
        self.code = code
        self.CPU = processor
        self.Local = Local
        self.mother = mo_name
        self.countdown = 0
        self.movement = 0
        self.name = ''
        self.length = len(code)

    def name(self) -> str:
        num = len(self.code)/2
        let = 'aaa'
        name = (str(num) + let)
        return name

    def isMother(self) -> bool:
        return True

    def isDaughter(self) -> bool:
        return False

    def geneology(self) -> str:
        return "HALP"

    def updateCountdown(self, cd):
        self.countdown = cd

