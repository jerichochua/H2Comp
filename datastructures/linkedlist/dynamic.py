#Linked List ADT - Dynamic V2
#Relevant link: http://interactivepython.org/runestone/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html

class Node:
    def __init__(self, data):
        self.data = data
        self.pointer = None

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getPointer(self):
        return self.pointer

    def setPointer(self, pointer):
        self.pointer = pointer

class LinkedList:
    def __init__(self):
        self.start = None

    def add(self, data):
        """Add new node at beginning of the linked list"""
        newNode = Node(data)
        newNode.setPointer(self.start)
        self.start = newNode

    def append(self, data):
        """Add new node at end of the linked list"""
        newNode = Node(data)
        current = self.start
        if current is None:
            self.start = newNode
        else:
            while current.getPointer() is not None:
                current = current.getPointer()
            current.setPointer(newNode)

    def insert(self, pos, data):
        """(INCOMPLETE) Insert new node in linked list at position pos"""
        newNode = Node(data)
        current = self.start
        previous = None

    def index(self, data):
        """Returns position of node in linked list if found, error otherwise"""
        current = self.start
        pos = 0
        found = False
        while current is not None:
            if current.getData() == data:
                found = True
                break
            else:
                pos += 1
                current = current.getPointer()

        if found:
            return pos
        else:
            return "Node not found"
    
    def size(self):
        """Returns size of linked list (number of nodes in linked list)"""
        current = self.start
        count = 0
        while current is not None:
            count += 1
            current = current.getPointer()
        return count

    def search(self, data):
        """Returns True if data is found in linked list, False otherwise"""
        current = self.start
        found = False
        while current is not None and not found:
            if current.getData() == data:
                found = True
            else:
                current = current.getPointer()
        return found

    def remove(self, data):
        """Remove node containing data in linked list"""
        current = self.start
        previous = None
        found = False
        while not found:
            if current.getData() == data:
                found = True
            else:
                previous = current
                current = current.getPointer()

        if previous is None:
            self.start = current.getPointer()
        else:
            previous.setPointer(current.getPointer())

    def pop(self):
        """Remove node at end of linked list and return its data"""
        current = self.start
        previous = None
        while current.getPointer() is not None:
            previous = current
            current = current.getPointer()

        if previous is None:
            self.start = None
        else:
            previous.setPointer(None)
        return current.getData()

    def display(self):
        """Displays all the nodes in the linked list"""
        current = self.start
        while current.getPointer() is not None:
            print(current.getData(), ">", end=" ")
            current = current.getPointer()
        print(current.getData())

    def isEmpty(self):
        """Returns True if linked list is empty, False otherwise"""
        return self.start is None

myList = LinkedList()
myList.add(31)
myList.add(77)
myList.add(17)
myList.add(93)
myList.add(26)
myList.add(54)
