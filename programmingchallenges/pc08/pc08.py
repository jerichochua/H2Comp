#Programming Challenge 8: Fruits Linked List

#Task 2
class ListNode:
    def __init__(self):
        self.DataValue = str("")
        self.PointerValue = int(0)

    def getDataValue(self):
        return self.DataValue

    def setDataValue(self, DataValue):
        self.DataValue = DataValue

    def getPointerValue(self):
        return self.PointerValue

    def setPointerValue(self, PointerValue):
        self.PointerValue = PointerValue

class LinkedList:
    def Initialise(self):
        """Initialises Node and values for Start and NextFree"""
        self.Node = [ListNode() for i in range(31)]
        for i in range(1, len(self.Node)-1):
             self.Node[i].setDataValue(str(""))
             self.Node[i].setPointerValue(int(i+1))
        
        self.Node[len(self.Node)-1].setDataValue(str(""))
        self.Node[len(self.Node)-1].setPointerValue(int(0))

        #Initialise values for Start and NextFree
        self.Start = int(0)
        self.NextFree = int(1)

    def DisplayLinkedList(self):
        """Displays all the nodes in the linked list"""
        print("self.Start = {0}, self.NextFree = {1}".format(self.Start, self.NextFree))
        print("|{0:^10}|{1:^20}|{2:^20}|".format("Node", "Data Value", "Pointer Value"))
        for i in range(1, len(self.Node)):
            print("|{0:^10}|{1:^20}|{2:^20}|".format(i, self.Node[i].getDataValue(), self.Node[i].getPointerValue()))

    def IsEmpty(self):
        """Returns True if linked list is empty, False otherwise"""
        return self.Start == 0

    def IsFull(self):
        """Returns True if linked list is full, False otherwise"""
        return self.NextFree == 0
    
    def AddNode(self):
        """Add a new node to the linked list"""
        NewItem = input("Enter new item: ")
        self.Node[self.NextFree].setDataValue(NewItem)

        if self.Start == 0:
            self.Start = self.NextFree
            Temp = self.Node[self.NextFree].getPointerValue()
            self.Node[self.NextFree].setPointerValue(0)
            self.NextFree = Temp
        else:
            #Traverse the list - starting at Start to find
            #the position at which to insert the new item
            Temp = self.Node[self.NextFree].getPointerValue()

            if NewItem < self.Node[self.Start].getDataValue():
                #New item will become the start of the list
                self.Node[self.NextFree].setPointerValue(self.Start)
                self.Start = self.NextFree
                self.NextFree = Temp
            else:
                #The new item is not at the start of the list
                Previous = 0
                Current = self.Start
                Found = False

                while not Found and Current != 0:
                    if NewItem <= self.Node[Current].getDataValue():
                        self.Node[Previous].setPointerValue(self.NextFree)
                        self.Node[self.NextFree].setPointerValue(Current)
                        self.NextFree = Temp
                        Found = True
                    else:
                        #Move on to the next node
                        Previous = Current
                        Current = self.Node[Current].getPointerValue()

                if Current == 0:
                    self.Node[Previous].setPointerValue(self.NextFree)
                    self.Node[self.NextFree].setPointerValue(0)
                    self.NextFree = Temp

    def TraversalInOrder(self, Index):
        """Performs an in-order traversal of the linked list"""
        if Index != 0:
            print(self.Node[Index].getDataValue())
            #Follow the pointer to the next data item in the linked list
            self.TraversalInOrder(self.Node[Index].getPointerValue())

    def Traversal(self):
        """Calls the TraversalInOrder procedure"""
        self.TraversalInOrder(self.Start)

    def TraversalInReverseOrder(self, Index):
        """Performs a reverse in-order traversal of the linked list"""
        if Index != 0:
            self.TraversalInReverseOrder(self.Node[Index].getPointerValue())
            print(self.Node[Index].getDataValue())

    def ReverseTraversal(self):
        """Calls the TraversalInReverseOrder procedure"""
        self.TraversalInReverseOrder(self.Start)
        
#Task 1
def main():
    fruitsList = LinkedList()
    fruitsList.Initialise()
    
    while True:
        print("1. Add an item")
        print("2. Traverse the linked list of used nodes and output the data values")
        print("3. Output all pointers and data values")
        print("4. Traverse linked list in reverse")
        print("5. Exit")

        option = input("Enter option: ")

        if option == "1":
            fruitsList.AddNode()
            print()
        elif option == "2":
            fruitsList.Traversal()
            print()
        elif option == "3":
            fruitsList.DisplayLinkedList()
            print()
        elif option == "4":
            fruitsList.ReverseTraversal()
            print()
        elif option == "5":
            break
        else:
            print("Invalid option entered.")

main()
