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

    def swap(self, i):
        bef = self.items.pop(i)
        self.items.insert(i + 1, bef)

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
        if self.soup.cells_alive > (.8 * len(self.soup.RAM)):
            death = self.reap.dequeue()
            d_cpu = self.soup.accessory[death]
            local = self.slicey.index(d_cpu)
            corpse = self.slicey.pop(local)
            begin = corpse.mem.start
            end = corpse.mem.length + begin
            corpse.countdown = 0
            for i in range(begin, end + 1):
                self.soup.property[i] = None
            self.soup.cells_alive -= 1


    def reapError(self, genotype: str) -> None:
        error1 = self.soup.err_library.get(genotype)
        i = self.reap.index(genotype)
        gen2 = self.reap.pop(i + 1)
        self.reap.insert(i + 1, gen2)
        error2 = self.soup.err_library.get(gen2)
        while error1 > error2:  # insert while loop until no champion
            self.reap.swap(i)
            i += 1
            if i < self.reap.size() - 1:
                gen2 = self.reap.pop(i + 1)
                self.reap.insert(i + 1, gen2)
                error2 = self.soup.err_library.get(gen2)
            else:
                break


    def slicer_increase(self, mother, daughter):
        # doles out small slices of CPU time to each creature in the soup .
        # Each creature has is created a CPU
        # daughter is just ahead of mother
        # number of instructions executed must be proportional to the size of the genome
        i = self.slicey.index(mother)
        self.slicey.insert(i + 1, daughter)

    def slicer_start(self, ancestor):
        self.slicey.enqueue(ancestor)
        length = int(.1 * ancestor.mem.length)
        ancestor.updateCountdown(length)  # how to make this specific to each
        while not self.slicey.isEmpty():
            self.slicer_rotate()

    def slicer_rotate(self):
        execute = self.slicey.rotate()  # gives file that is rotating and rotates queue
        length = int(.1 * execute.mem.length)
        execute.updateCountdown(length)  # how to make this specific to each
        execute.run()


    def cosmic_ray(self):
        ran = int(random.random() * len(self.soup.RAM))
        self.soup.RAM[ran] ^= 1

    def mutation(self, num):
        self.soup.RAM[num] ^= 1

    def find(self, size_genome):
        start = self.soup.total_length
        condition = False
        while not condition:
            for i in range(size_genome):
                if self.soup.property[start + i, 0] != 0:
                    start += i + 1
                    condition = False
                    break
            condition = True
        return start
