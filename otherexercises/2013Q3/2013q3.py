#NULL is 0

class Node:
    def __init__(self):
        self.LeftP = int(0) #Left pointer for the node
        self.Data = str("") #Node's data value
        self.RightP = int(0) #Right pointer for the node

    def getLeftP(self):
        return self.LeftP

    def getRightP(self):
        return self.RightP

    def getData(self):
        return self.Data

    def setLeftP(self, ptr):
        self.LeftP = ptr

    def setRightP(self, ptr):
        self.RightP = ptr

    def setData(self, data):
        self.Data = data

class BinaryTree:
    def __init__(self):
        self.ThisTree = [Node() for i in range(21)] #Tree data
        self.Root = int(0) #Index for root position of array
        self.NextFreePosition = int(1) #Index for next unused node
        #Set left pointers
        for i in range(1, len(self.ThisTree)):
            self.ThisTree[i].setLeftP(i+1)
        self.ThisTree[20].setLeftP(0)

    def AddItemIntoBinaryTree(self, NewFreeItem):
##        LastMove = "X"
##        CurrentPosition = 0
##        PreviousPosition = 0
        
        if self.NextFreePosition == 0: #Test if there is space available for new item
            return "No more space available for new item!"
        else:
            temp = self.ThisTree[self.NextFreePosition].getLeftP()
            if self.Root == 0: #If binary tree is empty
                self.Root = self.NextFreePosition
                self.ThisTree[self.NextFreePosition].setData(NewFreeItem)
                self.ThisTree[self.NextFreePosition].setLeftP(0)
                self.NextFreePosition = 2
                return
            else:
                #Traverse the tree to find the position for the new value
                CurrentPosition = self.Root
                LastMove = "X"
                while CurrentPosition != 0:
                    PreviousPosition = CurrentPosition
                    if NewFreeItem < self.ThisTree[CurrentPosition].getData():
                        #Move left
                        LastMove = "L"
                        self.ThisTree[self.NextFreePosition].setData(NewFreeItem)
                        CurrentPosition = self.ThisTree[CurrentPosition].getLeftP()
                    else:
                        #Move right
                        LastMove = "R"
                        self.ThisTree[self.NextFreePosition].setData(NewFreeItem)
                        CurrentPosition = self.ThisTree[CurrentPosition].getRightP()

            if LastMove == "R":
                self.ThisTree[PreviousPosition].setRightP(self.NextFreePosition)
            else:
                self.ThisTree[PreviousPosition].setLeftP(self.NextFreePosition)
            
            self.NextFreePosition = temp

            self.ThisTree[self.NextFreePosition-1].setLeftP(0) #Set left pointer to null

    def OutputData(self):
        print("Root:", self.Root)
        print("NextFreePosition:", self.NextFreePosition)
        print()
        print("{0:^8}|{1:^15}|{2:^15}|{3:^15}".format("Node", "Left Pointer", "Data", "Right Pointer"))
        for i in range(1, len(self.ThisTree)):
            print("{0:^8}|{1:^15}|{2:^15}|{3:^15}".format(i, self.ThisTree[i].getLeftP(), self.ThisTree[i].getData(), self.ThisTree[i].getRightP()))

    def inOrderTraversal(self, pointer=1):
        """Recursive in-order traversal"""
        if pointer != 0:
            self.inOrderTraversal(self.ThisTree[pointer].getLeftP())
            print(self.ThisTree[pointer].getData())
            self.inOrderTraversal(self.ThisTree[pointer].getRightP())
            
tree = BinaryTree()

def main():
    tree = BinaryTree()
    loop = True
    
    while loop:
        data = input("Enter an item: ")
        if data == "XXX":
            tree.OutputData()
            loop = False
        else:
            tree.AddItemIntoBinaryTree(data)

    print()
    tree.inOrderTraversal()

main()
