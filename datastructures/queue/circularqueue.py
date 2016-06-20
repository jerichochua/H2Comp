#Queue ADT - Circular Queue

class Queue:
    def __init__(self, limit):
        self.data = ["" for i in range(limit)]
        self.front = 0
        self.rear = limit-1
        self.size = 0
        self.limit = limit

    def __str__(self):
        return str(self.data)
    
    def insert(self, data):
        """Insert into rear of queue"""
        if self.size == self.limit: #Check if queue is full
            print("Queue overflow!")
            return
        else:
            if self.rear == self.limit - 1: #Check if rear pointer = limit
                self.rear = 0
            else:
                self.rear += 1 #Increment rear by 1
            self.data[self.rear] = data #Insert data into rear of queue
            self.size += 1 #Increment size by 1

    def remove(self):
        """Remove from front of queue"""
        if self.size == 0: #Check if queue is empty
            print("Queue underflow!")
            return
        else:
            self.data[self.front] = "" #Remove data
            self.size -= 1 #Decrement size by 1
            if self.front == self.limit - 1: #Check if front pointer = limit
                self.front = 0
            else:
                self.front += 1 #Increment front by 1
            
