RAM = [600000]
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

class Comp:
    def __init__(self):
        reap = Queue()

    def cpu(self):
        pass
    def reaper(self, file):
        self.reap.enqueue(file)
        if self.reap.size() > (.8 * len(RAM)):
            self.reap.dequeue()

    def slicer(self):
