class G_Memory:
    def __init__(self):
        self.RAM = bytearray(1000000) # soup
        self.bounds = range(len(self.RAM))
        self.property = {}  # index : genotype str
        self.accessory = {}  # genotype : Organism
        self.names = {} # length(str): num of names
        self.cells_alive = 0
        self.total_length = 0
        self.size = 60000
        self.total_instructions = 0
        self.err_library = {} # genotype: index

    def get(self, offset, value):
        assert offset in self.bounds, 'Memory.get: offset ({}) not in bounds ({})'.format(offset, self.bounds)
        size = len(value)
        assert offset + size in self.bounds, 'Memory.get: offset + size ({}) not in bounds ({})'.format(offset + size,
                                                                                                        self.bounds)

        return self.RAM[offset: offset + size]

    def set(self, offset, value):
        assert offset in self.bounds, 'Memory.get: offset ({}) not in bounds ({})'.format(offset, self.bounds)
        size = len(value)
        assert offset + size in self.bounds, 'Memory.get: offset + size ({}) not in bounds ({})'.format(offset + size,
                                                                                                        self.bounds)
        self.RAM[offset: offset + size] = value

    def fill(self, value):
        for i in range(len(self.RAM)):
            self.RAM[i] = value

    def add_length(self, size):
        self.total_length += size
