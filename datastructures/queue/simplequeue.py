#Queue ADT - Simple Implementation

class Queue:
    def __init__(self):
        self.data = []

    def isEmpty(self):
        """Returns True if queue is empty, False otherwise"""
        return len(self.data) is 0

    def enqueue(self, item):
        """Inserts new item into rear of queue (front of list)"""
        self.data.insert(0, item)

    def dequeue(self):
        """Removes and returns item from front of queue (rear of list)"""
        return self.data.pop()

    def size(self):
        """Returns size of the queue"""
        return len(self.data)

    def display(self):
        """Displays items in the queue"""
        print("{0:^25}".format("REAR OF QUEUE"))
        for i in range(len(self.data)):
            print("|{0:^25}|".format(self.data[i]))
        print("{0:^25}".format("FRONT OF QUEUE"))
