#Programming Challenge 5: Print Queue

#Task 2
def ValidateUserID(ThisUserID):
    if len(ThisUserID) != 9:
        return 1
    if not ThisUserID[0:4].isdigit() or not ThisUserID[5:9].isdigit():
        return 2
    if ThisUserID[0:4] != "2015":
        return 3
    return 0

#Task 3
class printQueue:
    def __init__(self, limit):
        self.data = [["" for i in range(3)] for j in range(limit)]
        self.front = 0
        self.rear = limit-1
        self.size = 0
        self.limit = limit

    def insert(self, userid, terminalno, size):
        printjob = [userid, terminalno, size]
        if self.size == self.limit:
            print("Print queue overflow.")
            return
        else:
            if self.rear == self.limit-1:
                self.rear = 0
            else:
                self.rear += 1
            self.data[self.rear] = printjob
            self.size += 1

    def remove(self):
        if self.size == 0:
            print("Print queue underflow.")
        else:
            self.data[self.front] = ["", "", ""]
            self.size -= 1
            if self.front == self.limit-1:
                self.front = 0
            else:
                self.front += 1

    def display(self):
        for i in range(len(self.data)):
            print("{0}. {1}".format(i+1, self.data[i]))

#Task 4
def menu():
    maxqueueSize = 5
    Room14 = printQueue(maxqueueSize)

    while True:
        print("1. New print job added to print queue")
        print("2. Next print job output from printer")
        print("3. Current print queue displayed")
        print("4. End")

        option = input("Enter option: ")
        if option == "1":
            userid = input("Enter User ID: ")
            if ValidateUserID(userid) == 0:
                terminalno = input("Enter terminal number: ")
                if int(terminalno) < 1 or int(terminalno) > 172:
                    print("Terminal number out of range.")
                    print()
                    continue
                size = input("Enter file size (in Kbytes): ")
                Room14.insert(userid, terminalno, size)
                print("New print job added.")
                print()
            else:
                print("User ID not valid.")
                print()
        elif option == "2":
            Room14.remove()
            print("Print job removed.")
            print()
        elif option == "3":
            print("Current print queue:")
            Room14.display()
            print()
        elif option == "4":
            break
        else:
            print("Invalid option entered.")
            print()
