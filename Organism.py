class Organism:
    def __init__(self, code, CPU):
        self.error_fault = 0
        self.code = code
        self.CPU = CPU
        self.mother = 'original'

    def isMother(self) -> bool:
        return True
    def isDaughter(self) -> bool:
        return False
    def geneology(self) -> str:
        return "HALP"

