# Insertion Sort

myList = [94, 12, 53, 25, 36, 75]

def InsertionSort(myList):
    for index in range(1, len(myList)):
        current = myList[index]

        while index > 0 and current < myList[index-1]:
            myList[index] = myList[index-1]
            index -= 1

        myList[index] = current
        print(myList)
    print(myList)

InsertionSort(myList)

