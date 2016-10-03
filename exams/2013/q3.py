# Question 3

# Task 3.1
class Node:
    def __init__(self):
        self.__LeftP = int(0)
        self.__Data = str('')
        self.__RightP = int(0)

    def getLeftP(self):
        return self.__LeftP

    def setLeftP(self, LeftP):
        self.__LeftP = LeftP

    def getData(self):
        return self.__Data

    def setData(self, Data):
        self.__Data = Data

    def getRightP(self):
        return self.__RightP

    def setRightP(self, RightP):
        self.__RightP = RightP

class BinaryTree:
    def __init__(self):
        self.ThisTree = [Node() for i in range(21)]
        self.Root = int(0)
        self.NextFreePosition = int(1)

        for i in range(1, len(self.ThisTree)-1):
            self.ThisTree[i].setLeftP(int(i+1))
            self.ThisTree[i].setData('')
            self.ThisTree[i].setRightP(int(0))

    # Task 3.2
    def AddItemToBinaryTree(self, NewTreeItem):
        if self.NextFreePosition == 0:
            print('No more space available for new item.')
        if self.Root == 0:
            self.Root = self.NextFreePosition
            self.ThisTree[self.Root].setData(NewTreeItem)
            self.ThisTree[self.Root].setLeftP(0)
            self.NextFreePosition = 2
            return
        else:
            temp = self.ThisTree[self.NextFreePosition].getLeftP()
            #traverse the tree to find the position for the new value
            CurrentPosition = self.Root
            LastMove = 'X'
            while CurrentPosition != 0:
                PreviousPosition = CurrentPosition
                if NewTreeItem < self.ThisTree[CurrentPosition].getData():
                    #move left
                    LastMove = 'L'
                    CurrentPosition = self.ThisTree[CurrentPosition].getLeftP()
                    self.ThisTree[self.NextFreePosition].setData(NewTreeItem)
                else:
                    #move right
                    LastMove = 'R'
                    CurrentPosition = self.ThisTree[CurrentPosition].getRightP()
                    self.ThisTree[self.NextFreePosition].setData(NewTreeItem)

        if LastMove == 'R':
            self.ThisTree[PreviousPosition].setRightP(self.NextFreePosition)
        else:
            self.ThisTree[PreviousPosition].setLeftP(self.NextFreePosition)
        self.NextFreePosition = temp
        self.ThisTree[self.NextFreePosition-1].setLeftP(0)

    # Task 3.3
    def OutputData(self):
        print('self.Root = {}, self.NextFreePosition = {}'.format(self.Root, self.NextFreePosition))
        print('|{0:^8}|{1:^12}|{2:^20}|{3:^12}|'.format('Node', 'Left Ptr', 'Data', 'Right Ptr'))
        for i in range(1, len(self.ThisTree)):
            print('|{0:^8}|{1:^12}|{2:^20}|{3:^12}|'.format(i, self.ThisTree[i].getLeftP(), self.ThisTree[i].getData(), self.ThisTree[i].getRightP()))

    # Task 3.6
    def inOrderTraversal(self, pointer=1):
        """Recursive in-order traversal"""
        if pointer != 0:
            self.inOrderTraversal(self.ThisTree[pointer].getLeftP())
            print(self.ThisTree[pointer].getData())
            self.inOrderTraversal(self.ThisTree[pointer].getRightP())

# Task 3.4/3.5
def main():
    countries = BinaryTree()
    
    loop = True
    while loop:
        country = input('Enter country (XXX to terminate): ').upper()

        if country != 'XXX':
            countries.AddItemToBinaryTree(country)
        else:
            countries.OutputData()
            loop = False
    print()
    countries.inOrderTraversal()


main()
