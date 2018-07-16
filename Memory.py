class G_Memory:
    def __init__(self):
        self.RAM = [0x00] * 60000 # soup
        self.property = {}  # index : genotype str
        self.accessory =  {}  # genotype : Organism
        self.num_cells = 1
        self.total_instructions = 0
        self.err_library = {'80aaa': 0} # genotype: error
        self.slicer_lib = {} # genotype: index

    def get_RAM(self):
        return self.RAM

    def get(self, offset, value):
        size = len(value)
        return self.RAM[offset: offset + size]

    def set(self, offset, value):
        size = len(value)
        self.RAM[offset: offset + size] = value
    def fill(self, value):
        for i in range(len(self.RAM)):
            self.RAM[i] = value