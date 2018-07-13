import random
from Memory import G_Memory
from Organism import Organism
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def swap(self, i, dir):
        if dir is 1:
            bef = self.items.pop(i + 1)
            self.items.insert(i, bef)
        elif dir is 0:
            bef = self.item.pop(i)
            self.items.insert(i, bef)

    def index(self, element):
        return self.items.index(element)

    def size(self):
        return len(self.items)


class Circle(Queue):
    def __init__(self):
        super(Circle, self).__init__(self)


    def rotate(self):
        val = self.items.pop()
        self.items.enqueue(val)
        return val


class operating_system:
    def __init__(self, mem: G_Memory):
        self.reap = Queue()
        self.slice = Circle() # System maintains a circular queue
        self.soup = mem

    def cellularity(self, genotype: str) -> None: # Memory Allocation: As in will give rights to land for a genotype
        # Each creature has exclusive write privilege: Mother and Daughter(MAL- memory allocation)
        # size of creature = size of genome (allocated block)
        # Divide: mother loses write privileges;  daughter cell is given its own IP, free allocate second block
        beg = self.soup.library[genotype]
        end = int(genotype[0:2]) + beg + 1
        for i in range(beg, end):
            self.soup.property[i] = True


    def insert_Fam(self, mother, daughter) -> None:
        self.soup.families[mother] = daughter


    def isOwned(self, beg, end) -> bool:
        for i in range(beg, end):
            if self.soup.property[i] == True:
                return True
        return False


    def isOwned(self, index) -> bool:
        if self.soup.library[index] == True:
            return True
        else:
            return False

    def reapUpdate(self, file):
        self.reap.enqueue(file)
        if self.reap.size() > (.8 * len(self.soup.RAM)):
            self.reap.dequeue()
            self.slice.dequeue()

    def reapError(self, genotype: str) -> None:
        error1 = self.soup.err_library.get(genotype)
        i = self.reap.index(genotype)
        gen2 = self.reap.pop(i + 1)
        self.reap.insert(i + 2, gen2)
        error2 = self.soup.err_library.get(gen2)
        while error1 > error2: # insert while loop until no champion
            self.reap.swap(genotype)
            i += 1
            gen2 = self.reap.pop(i + 1)
            self.reap.insert(i + 2, gen2)
            error2 = self.soup.err_library.get(gen2)

    def slicer_increase(self, mother: Organism, daughter: Organism):
        # doles out small slices of CPU time to each creature in the soup .
        # Each creature has is created a CPU
        # daughter is just ahead of mother
        # number of instructions executed must be proportional to the size of the genome
        i = self.slice.index(mother)
        self.slice.insert(i + 1, daughter)

    def slicer_rotate(self):
        execute = slice.rotate(self)  # gives file that is rotating and rotates queue
        length = int(.25 * int(execute[0:2]))
        execute.updateCountdown(length)  # how to make this specific to each

    def mutation(self):
         ran = random.random()
         bit = self.soup.RAM_bit[ran]
         bit ^= 1
         bit = self.soup.RAM_bit[ran]

    def mutation(self, org: Organism):
        bit = self.org.Lo