#Bubble Sort

myList = [94, 12, 53, 25, 36, 75]

def BubbleSort(myList):
    for i in range(len(myList)-1):
        for j in range(len(myList)-1):
            if myList[j] > myList[j+1]:
                myList[j], myList[j+1] = myList[j+1], myList[j]

    print(myList)

BubbleSort(myList)
