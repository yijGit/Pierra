from vm import CPU
from Memory import G_Memory
from OS import operating_system
class Organism:
    def __init__(self, code, processor: CPU, mem: G_Memory, OS: operating_system, mo_name: str):
        self.error_fault = 0
        self.code = code
        self.CPU = processor
        self.RAM = mem
        self.OS = OS
        self.mother = mo_name
        self.countdown = 0
        self.movement = 0
        self.name = ''

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

