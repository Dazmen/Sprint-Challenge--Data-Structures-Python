from collections import deque

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = deque()
        self.pointer = 0

    def append(self, item):
        if len(self.storage) >= self.capacity:
            self.storage[self.pointer] = item
            if self.pointer == self.capacity - 1:
                self.pointer = 0
            else:
                self.pointer += 1
        else:
            self.storage.append(item)


    def get(self):
        return [i for i in self.storage if i is not None]