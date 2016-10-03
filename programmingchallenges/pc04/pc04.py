# Programming Challenge 4: Pond
# A-Levels 2014 Q4

def createPond(): # Initialise pond
    pond = [["." for i in range(15)] for j in range(8)]
    return pond

def displayPond(pond): # Display pond
    for i in range(8):
        for j in range(15):
            print(pond[i][j], end="")
        print()

# Task 2
def throwStone():
    pond = createPond()
    posX = eval(input("X coordinate <1 to 15>? "))
    if posX < 1 or posX > 15:
        return "out of range"
    posY = eval(input("Y coordinate <1 to 8>? "))
    if posY < 1 or posY > 8:
        return "out of range"

    pond[posY-1][posX-1] = "S"
    displayPond(pond)

# Task 3
def fishes():
    import random
    pond = createPond()
    fishPos = []
    
    for i in range(3):
        fishposX = random.randint(1,15)
        fishposY = random.randint(1,8)
        while (fishposX, fishposY) in fishPos: # Ensures 2 fish do not occupy 1 space
            fishposX = random.randint(1,15)
            fishposY = random.randint(1,8)
        fishPos.append((fishposX, fishposY)) # Append fish position (as tuple) to list
        pond[fishposY-1][fishposX-1] = "F"
    displayPond(pond)

# Task 4
def feeding():
    import random
    pond = createPond()

    # Allow user input for coordinates and validate input
    posX = eval(input("X coordinate <1 to 15>? "))
    if posX < 1 or posX > 15:
        return "out of range"
    posY = eval(input("Y coordinate <1 to 8>? "))
    if posY < 1 or posY > 8:
        return "out of range"
    
    fishPos = []
    for i in range(3):
        fishposX = random.randint(1,15)
        fishposY = random.randint(1,8)
        while (fishposX, fishposY) in fishPos: # Ensures 2 fish do not occupy 1 space
            fishposX = random.randint(1,15)
            fishposY = random.randint(1,8)
        fishPos.append((fishposX, fishposY)) # Append fish position (as tuple) to list
        pond[fishposY-1][fishposX-1] = "F"

    if pond[posY-1][posX-1] == "F": # Check if position has fish
        pond[posY-1][posX-1] = "H"
    else:
        pond[posY-1][posX-1] = "P"

    displayPond(pond)
