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

class Comp:
    def __init__(self):
        reap = Queue()
        slice = Circle()
        RAM = [0] * 600000

    def reaper(self, file):
        self.reap.enqueue(file)
        if self.reap.size() > (.8 * len(self.RAM)):
            self.reap.dequeue()

    def slicer(self, names):
        self.slice.enqueue(names)

    class CPU():
        def __init__(self):
            pass
        def fetch(self):
            pass
        def decode(self):
            pass
        def execute(self):
            pass
