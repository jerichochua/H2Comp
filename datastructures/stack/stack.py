# Stack ADT V2

class Stack():
    def __init__(self):
        self.data = []

    def isEmpty(self):
        """Returns True if stack is empty, False otherwise"""
        return len(self.data) == 0

    def push(self, data):
        """Push data into stack"""
        self.data.append(data)

    def pop(self):
        """Pop top data out of stack"""
        return self.data.pop()

    def peek(self):
        """Returns top of stack"""
        return self.data[len(self.data)-1]

    def size(self):
        """Returns size of stack"""
        return len(self.data)

    def display(self):
        """Displays stack"""
        for i in range(len(self.data)-1, -1, -1):
            print("|{0:^18}|".format(self.data[i]))
        print("-"*20)
