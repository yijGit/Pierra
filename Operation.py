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

    def elementAt(self, index):
        return self.items[index]

    def size(self):
        return len(self.items)


class Circle(Queue):
    def __init__(self):
        super(Circle, self).__init__()

    def rotate(self):
        val = self.items.pop()
        self.enqueue(val)
        return val


class operating_system:
    def __init__(self, memory: G_Memory):
        self.reap = Queue()
        self.slicey = Circle() # System maintains a circular queue
        self.soup = memory

    def reapUpdate(self, file): # uses names
        self.reap.enqueue(file)
        self.soup.cells_alive += 1
        if self.soup.cells_alive > (.05 * len(self.soup.RAM)):
            print(self.slicey.size())
            death = self.reap.dequeue()
            local = self.slicey.index(death)
            corpse = self.slicey.pop(local)
            cor_cpu = self.soup.accessory[corpse]
            print(self.slicey.size())
            begin = cor_cpu.mem.start
            end = cor_cpu.mem.length + begin
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

        i = self.slicey.index(mother)
        self.slicey.insert(i + 1, daughter)

    def slicer_start(self, ancestor):
        self.slicey.enqueue(ancestor)
        anc_cpu = self.soup.accessory[ancestor]
        length = int(.1 * anc_cpu.mem.length)
        anc_cpu.updateCountdown(length)  # how to make this specific to each
        while not self.slicey.isEmpty():
            self.slicer_rotate()

    def slicer_rotate(self):
        execute = self.slicey.rotate()  # gives file that is rotating and rotates queue
        exe_cpu = self.soup.accessory[execute]
        length = int(.1 * exe_cpu.mem.length)
        exe_cpu.updateCountdown(length)  # how to make this specific to each
        exe_cpu.run()

    def cosmic_ray(self):
        ran = int(random.random() * len(self.soup.RAM))
        self.soup.RAM[ran] ^= 1

    def mutation(self, num):
        self.soup.RAM[num] ^= 1
