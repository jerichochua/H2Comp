#Linked List ADT - Array Implementation

class Node:
    def __init__(self):
        self.__data = ""
        self.__pointer = int(0)

    def getData(self):
        return self.__data

    def setData(self, data):
        self.__data = data

    def getPointer(self):
        return self.__pointer

    def setPointer(self, pointer):
        self.__pointer = pointer

    def __str__(self):
        return self.__data

class LinkedList:
    def initialise(self, maxnum):
        self.start = int(-1)
        self.nextfree = int(0)
        self.arrayofnodes = [Node() for i in range(maxnum)]
        for i in range(maxnum):
            self.arrayofnodes[i].setPointer(i+1)
        self.arrayofnodes[maxnum-1].setPointer(int(-1))

    def Display(self):
        print("start = {0}, nextfree = {1}".format(self.start, self.nextfree))
        print("{0:^6}|{1:^20}|{2:^10}".format("NODE", "DATA", "POINTER"))
        for i in range(len(self.arrayofnodes)):
            print("{0:^6}|{1:^20}|{2:^10}".format(i, self.arrayofnodes[i].getData(), self.arrayofnodes[i].getPointer()))
    
    def insert_node(self, new_value):
        """Add new node into linked list"""
        if self.nextfree == -1: #Checks if free node exist
            print("No more space to insert.")
            return
        else:
            self.arrayofnodes[self.nextfree].setData(new_value) #Store new_value in nextfree node
            if self.start == -1:
                holdfree = self.arrayofnodes[self.nextfree].getPointer()
                self.arrayofnodes[self.nextfree].setPointer(int(-1))
                self.start = self.nextfree
                self.nextfree = holdfree
            else:
                if new_value < self.arrayofnodes[self.start].getData(): #Insert as first node of list
                    holdfree = self.arrayofnodes[self.nextfree].getPointer()
                    self.arrayofnodes[self.nextfree].setPointer(self.start)
                    self.start = self.nextfree
                    self.nextfree = holdfree
                else:                
                    previous = self.start
                    current = self.start
                    while new_value > self.arrayofnodes[current].getData() and self.arrayofnodes[current].getPointer() != -1:
                        previous = current
                        current = self.arrayofnodes[current].getPointer()
                    if new_value > self.arrayofnodes[current].getData() and self.arrayofnodes[current].getPointer() == -1: #Insert at last node of list
                        holdfree = self.arrayofnodes[self.nextfree].getPointer()
                        self.arrayofnodes[current].setPointer(self.nextfree)
                        self.arrayofnodes[self.nextfree].setPointer(int(-1))
                        self.nextfree = holdfree
                    else: #Insert inbetween nodes
                        holdfree = self.arrayofnodes[self.nextfree].getPointer()
                        self.arrayofnodes[previous].setPointer(self.nextfree)
                        self.arrayofnodes[self.nextfree].setPointer(current)
                        self.nextfree = holdfree

    def delete_node(self, delete_value):
        """Remove node from linked list"""
        if self.start == -1:
            print("List is empty.") #Check if list is empty
            return
        if self.arrayofnodes[self.start].getData() == delete_value: #First node to be deleted
            current = self.arrayofnodes[self.start].getPointer()
            self.arrayofnodes[self.start].setPointer(self.nextfree)
            self.arrayofnodes[self.start].setData("")
            self.nextfree = self.start
            self.start = current
        else:
            previous = self.start
            current = self.arrayofnodes[previous].getPointer()
            if self.arrayofnodes[current].getPointer() == -1:
                print("Node not found.")
                return
            while self.arrayofnodes[current].getData() != delete_value:
                previous = current
                current = self.arrayofnodes[current].getPointer()
                if current == -1:
                    print("Node not found.")
                    return
            self.arrayofnodes[previous].setPointer(self.arrayofnodes[current].getPointer())
            self.arrayofnodes[current].setData("")
            self.arrayofnodes[current].setPointer(self.nextfree)
            self.nextfree = current

    def search_node(self, search_value):
        """Search for node in linked list"""
        if self.start == -1:
            print("List is empty.") #Check if list is empty
            return
        if self.arrayofnodes[self.start].getData() == search_value: #First node to be deleted
            current = self.arrayofnodes[self.start].getPointer()
            self.arrayofnodes[self.start].setPointer(self.nextfree)
            self.arrayofnodes[self.start].setData("")
            self.nextfree = self.start
            self.start = current
        else:
            previous = self.start
            current = self.arrayofnodes[previous].getPointer()
            if self.arrayofnodes[current].getPointer() == -1:
                print("Node not found.")
                return
            while self.arrayofnodes[current].getData() != delete_value:
                previous = current
                current = self.arrayofnodes[current].getPointer()
                if current == -1:
                    print("Node not found.")
                    return

def menu():
    while True:
        print("Linked List Menu")
        print("===================")
        print("1. Initialise\n2. Insert data\n3. Delete data\n4. Display linked list\n5. Search data\n6. Exit")
        choice = input("Enter selection: ")
        print("")
        if choice == "1":
            L = LinkedList()
            maxnum = eval(input("Enter maximum number of nodes: "))
            L.initialise(maxnum)
            print("Linked list initialised.")
            print("")
        elif choice == "2":
            value = input("Enter value to be inserted: ")
            L.insert_node(value)
            print("")
        elif choice == "3":
            value = input("Enter value to be deleted: ")
            L.delete_node(value)
            print("")
        elif choice == "4":
            L.Display()
            print("")
        elif choice == "5":
            value = input("Enter value to be searched: ")
            L.search_node(value)
            print("")
        elif choice == "6":
            break
        else:
            print("Error - wrong selection.")
            print("")

menu()
