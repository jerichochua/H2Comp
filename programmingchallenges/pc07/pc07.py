# Programming Challenge 7: Game Linked List

class Node:
    def __init__(self, playerID, score):
        self.playerID = str(playerID)
        self.score = int(score)
        self.ptr = None

    def getplayerID(self):
        return self.playerID

    def setplayerID(self, playerID):
        self.playerID = playerID

    def getScore(self):
        return self.score

    def setScore(self, score):
        self.score = score

    def getPointer(self):
        return self.ptr

    def setPointer(self, ptr):
        self.ptr = ptr

class LinkedList:
    def __init__(self):
        self.start = None
        
    def validateScore(self, score):
        """Validates score"""
        if score.isdigit() and int(score) >= 0 and int(score) <= 20:
            return True
        else:
            return False

    def validatePlayerID(self, playerID):
        """Validates player ID"""
        if len(playerID) >= 3 and playerID[0].isalpha():
            return True
        else:
            return False

    def checkPlayer(self, playerID):
        """Returns True if player exists in linked list, False otherwise"""
        current = self.start
        while current is not None:
            if current.getplayerID() == playerID:
                return True
            current = current.getPointer()
        return False

    def getScore(self, playerID):
        """Returns score of player, given player ID"""
        current = self.start
        while current.getplayerID() != playerID:
            current = current.getPointer()
        return current.getScore()

    def getRank(self, playerID):
        """Returns rank of player, given player ID"""
        rank = 1
        current = self.start
        previous = None
        while current.getPointer() is not None and current.getplayerID() != playerID:
            previous = current
            current = current.getPointer()
            if previous.getScore() != current.getScore():
                rank += 1

        if current.getplayerID() == playerID:
            return rank
        else:
            return None

    def getMaxRank(self):
        """Returns maximum ranking in linked list"""
        if self.start is None:
            return None
        else:
            maxRank = 1
            current = self.start
            previous = None
            while current.getPointer() is not None:
                previous = current
                current = current.getPointer()
                if previous.getScore() != current.getScore():
                    maxRank += 1
            return maxRank

    def addPlayer(self, playerID, score):
        """Adds a new player into linked list, highest score first"""
        newNode = Node(playerID, score)
        if self.start is None:
            self.start = newNode
        else:
            current = self.start
            previous = None
            while current is not None and newNode.getScore() <= current.getScore():
                if newNode.getScore() == current.getScore():
                    if newNode.getplayerID() < current.getplayerID():
                        break
                previous = current
                current = current.getPointer()

            if current is None:
                previous.setPointer(newNode)
            else:
                if previous is None:
                    temp = current
                    self.start = newNode
                    newNode.setPointer(temp)
                else:
                    previous.setPointer(newNode)
                    newNode.setPointer(current)
    
    def removePlayer(self, playerID):
        """Removes a player from the linked list"""
        current = self.start
        previous = None
        while current.getplayerID() != playerID:
            previous = current
            current = current.getPointer()

        if previous is None:
            self.start = current.getPointer()
        else:
            previous.setPointer(current.getPointer())

    def updatePlayer(self, playerID, score):
        """Updates a player in the linked list"""
        if self.validatePlayerID(playerID) and self.validateScore(score):
            print("Old rank: ", self.getRank(playerID))
            if self.checkPlayer(playerID):
                newScore = self.getScore(playerID) + int(score)
                self.removePlayer(playerID)
                self.addPlayer(playerID, newScore)
            else:
                self.addPlayer(playerID, score)
            print("New rank: ", self.getRank(playerID))
        else:
            print("Invalid input.")

    def display(self):
        """Displays all the nodes in the linked list"""
        current = self.start
        while current.getPointer() is not None:
            print(current.getplayerID(), current.getScore(), ">", end=" ")
            current = current.getPointer()
        print(current.getplayerID(), current.getScore())

    # Task 3
    def validateRankRange(self, rankrange):
        """Validates rank range"""
        lower, upper = rankrange.split("-")
        if lower.isdigit() and upper.isdigit():
            if int(lower) > 0 and int(upper) > 0:
                if int(upper) <= self.getMaxRank():
                    return True
        else:
            return False

    def displayRank(self, rankrange):
        """Displays nodes in the linked list that are within rank range"""
        rankList = []
        rankCount = {}
        if self.validateRankRange(rankrange):
            lower, upper = rankrange.split("-")
            lower = int(lower)
            upper = int(upper)
            current = self.start
            while current is not None:
                currentRank = self.getRank(current.getplayerID())
                if currentRank >= lower and currentRank <= upper:
                    rankList.append((currentRank, current.getplayerID()))
                    rankCount[currentRank] = rankCount.get(currentRank, 0) + 1
                current = current.getPointer()

            # Display rank and player ID
            print("{0:^25}".format("Ranking"))
            print("-"*25)
            print("{0:^5}{1}{2:^20}".format("Rank", "|", "Player ID"))
            for data in rankList:
                print("{0:^5}{1}{2:^20}".format(data[0], "|", data[1]))
            print()

            # Display rank count
            print("{0:^25}".format("Rank Count"))
            print("-"*25)
            for rank in range(lower, upper+1):
                if rank not in rankCount:
                    break
                print("Rank #{0}: {1}".format(rank, rankCount[rank]))
            
        else:
            print("Invalid input.")
    
def main():
    loop = True
    while loop:
        print("Game Linked List Menu")
        print("1. Create linked list from file")
        print("2. Display linked list")
        print("3. Update player ID and score")
        print("4. Remove player")
        print("5. Enter rank range")
        print("9. Quit")
        print()
        option = input("Enter a choice: ")

        if option == "1":
            scores = open("GAME.DAT", "r")
            gamelist = LinkedList()
            for score in scores:
                playerid, score = score.rstrip().split()
                gamelist.addPlayer(playerid, score)
            scores.close()
            print("Linked list created from GAME.DAT.")
            print()
        elif option == "2":
            gamelist.display()
            print()
        elif option == "3":
            playerid = input("Enter player ID: ")
            score = input("Enter score: ")
            gamelist.updatePlayer(playerid, score)
            print()
        elif option == "4":
            playerid = input("Enter player ID: ")
            gamelist.removePlayer(playerid)
            print()
        elif option =="5":
            rankrange = input("Enter rank range (x-y): ")
            gamelist.displayRank(rankrange)
            print()
        elif option == "9":
            break
        else:
            print("Invalid option.")

main()
