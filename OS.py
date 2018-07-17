import random
from Memory import G_Memory
# from CPU import CPU


class Queue:


    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def insert(self, num, item):
        self.items.insert(num, item)

    def dequeue(self):
        return self.items.pop()

    def pop(self, num):
        return self.items.pop(num)

    def swap(self, i, num):
        if num is 1:
            bef = self.items.pop(i + 1)
            self.items.insert(i, bef)
        elif num is 0:
            bef = self.items.pop(i)
            self.items.insert(i, bef)

    def index(self, element):
        return self.items.index(element)

    def size(self):
        return len(self.items)


class Circle(Queue):
    def __init__(self):
        super(Circle, self).__init__()

    def rotate(self):
        val = self.items.pop()
        self.items.insert(0, val)
        return val


class operating_system:
    def __init__(self, memory: G_Memory):
        self.reap = Queue()
        self.slice = Circle() # System maintains a circular queue
        self.soup = memory

    def reapUpdate(self, file):
        self.reap.enqueue(file)
        if self.soup.cells_alive > (.8 * len(self.soup.RAM)):
            death = self.reap.dequeue()
            local = self.slice.index(death)
            corpse = self.slice.pop(local)
            begin = corpse.mem.start
            end = corpse.mem.length + begin
            for i in range(begin, end + 1):
                self.soup.property[i] = None
            self.soup.cells_alive -= 1


    def reapError(self, genotype: str) -> None:
        error1 = self.soup.err_library.get(genotype)
        i = self.reap.index(genotype)
        gen2 = self.reap.pop(i + 1)
        self.reap.insert(i + 2, gen2)
        error2 = self.soup.err_library.get(gen2)
        while error1 > error2: # insert while loop until no champion
            self.reap.swap(genotype, 0)
            i += 1
            gen2 = self.reap.pop(i + 1)
            self.reap.insert(i + 2, gen2)
            error2 = self.soup.err_library.get(gen2)


    def slicer_increase(self, mother, daughter):
        # doles out small slices of CPU time to each creature in the soup .
        # Each creature has is created a CPU
        # daughter is just ahead of mother
        # number of instructions executed must be proportional to the size of the genome
        i = self.slice.index(mother)
        self.slice.insert(i + 1, daughter)

    def slicer_rotate(self):
        execute = self.slice.rotate()  # gives file that is rotating and rotates queue
        length = .1 * execute.mem.length()
        execute.mem.updateCountdown(length)  # how to make this specific to each
        execute.run()

    def cosmic_ray(self):
        ran = random.random() * len(self.soup.RAM)
        self.soup.RAM[ran] ^= 1

    def mutation(self, num):
        self.soup.RAM[num] ^= 1