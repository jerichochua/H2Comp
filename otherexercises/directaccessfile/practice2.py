maxAddress = 13

# Task 2
def HashingFunction(fruit):
    value = int(0)
    for letter in fruit:
        value = value + ord(letter)
    address = value % maxAddress + 1
    return address

def StoreFruit():
    fruitList = [] #Initialise list of fruits
    addressList = [] #Initialise list of addresses

    outfile = open("NEWFILE3.TXT", "w+")

    # Get list of fruits
    loop = True
    while loop:
        fruit = input("Enter fruit: ")
        if fruit == "XXX":
            loop = False
        else:
            fruitList.append(fruit)

    # Get address of item
    for fruit in fruitList:
        address = HashingFunction(fruit)

        # Collision resolution - Quadratic probing
        num = 1
        while address in addressList:
            address = address + num**2
            while address > 13:
                address = address - maxAddress
            num += 1
            print("New address:", address)

        addressList.append(address)
        location = (address-1)*20 # Get location of item
        record = fruit.ljust(20," ")
        outfile.seek(location) # Go to location in file
        outfile.write(record) # Write to location in file

    outfile.close()

# Task 3
def LookupFruit():
    infile = open("NEWFILE3.TXT", "r")
    inputFruit = input("Enter a fruit: ")

    address = HashingFunction(inputFruit) #Get address
    location = (address-1)*20 #Get location

    infile.seek(location) #Go to location of record
    fruit = infile.readline()[0:20].strip(" ")

    collisions = 0
    while inputFruit != fruit:
        if address == 13:
            address = 1
            collisions += 1
        else:
            address = address + 1
            collisions = collisions + 1

        location = (address-1)*30
        infile.seek(location)

        fruit = infile.readline()[0:20].strip(" ")

        if collisions > 13:
            print("{0} not found.".format(inputFruit))
            break

    if collisions <= 13:
        print("{0} found at address {1}.".format(inputFruit, address))

    infile.close()
