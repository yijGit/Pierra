import random
from Memory import G_Memory
class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

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
    def __init__(self):
        reap = Queue()
        slice = Circle() # System maintains a circular queue
        read = 0

    def cellularity(self, genotype): # Memory Allocation: As in will give rights to land for a genotype
        # Each creature has exclusive write privilege: Mother and Daughter(MAL- memory allocation)
        # size of creature = size of genome (allocated block)
        # Divide: mother loses write privileges;  daughter cell is given its own IP, free allocate second block


    def reaper(self, file):
        self.reap.enqueue(file)
        if self.reap.size() > (.8 * len(self.RAM)):

            self.reap.dequeue()
            self.slice.dequeue()

    def slicer(self, names):
        # doles out small slices of CPU time to each creature in the soup .
        # Each creature has is created a CPU
        # daughter is just ahead of mother
        # number of instructions executed must be proportional to the size of the gneome
        self.slice.enqueue(names)

    def mutation(self):
        if self.read > 60000:
            random.random()*60000
