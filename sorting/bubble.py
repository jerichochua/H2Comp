#Bubble Sort

myList = [94, 12, 53, 25, 36, 75]

def BubbleSort(myList):
    for i in range(len(myList)):
        for j in range(len(myList)):
            if myList[i] < myList[j]:
                myList[i], myList[j] = myList[j], myList[i]
                # temp = myList[i]
                # myList[i] = myList[j]
                # myList[j] = temp
    print(myList)

BubbleSort(myList)
