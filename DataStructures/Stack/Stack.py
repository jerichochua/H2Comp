class Stack: #Stack implementation - Data added to rear of list
    def __init__(self): #Initialise
        self.data = [] #Initialise empty list

    def __str__(self):
        text = ""
        for i in range(len(self.data)-1, -1, -1):
            text = text + "\n" + "{0}".format(self.data[i])
        text = text + "\n---------------"
        return text

    def push(self, data): #Push data into stack
        self.data.append(data)

    def pop(self): #Pop data out of stack
        self.data.pop()

    def peek(self): #Look at top item of stack
        return self.data[len(self.data)-1]

    def size(self): #Return size of stack
        return len(self.data)

    def isEmpty(self): #Check if stack is empty
        return len(self.data) == 0
