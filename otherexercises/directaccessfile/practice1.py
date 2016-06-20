# A - Address of record
# K - key value of record
# M - maximum address space allocated

M = 47

# Task 1
def HashAsia(country):
    K = int(0)
    for letter in country:
        K = K + ord(letter)
    A = K % M + 1
    return A

# Task 2
def GetOne():
    infile = open("asia.csv", "r")
    infile.readline()[:-1] #To get rid of the header
    country, population = infile.readline().rstrip().split(",") #Read first country name and population
    infile.close()

    address = HashAsia(country) #Generate address for country
    location = (address-1)*30
    record = country.ljust(20,"#") + population.ljust(10,"#")

    outfile = open("NEWFILE1.TXT", "w+")
    outfile.seek(location)
    outfile.write(record)
    outfile.close()

# Task 3
def GetAll():
    addressList = [] #Store addresses in a list
    
    infile = open("asia.csv", "r")
    outfile = open("NEWFILE1.TXT", "w+")
    infile.readline()[:-1] #To get rid of header
    
    for line in infile:
        country, population = line.rstrip().split(",") #Read country and population
        address = HashAsia(country)

        # Collision resolution - Linear probing
        while address in addressList:
            if address == 47: #Check if address is maximum address
                address = 1
            else:
                address = address + 1
  
        addressList.append(address)
        location = (address-1)*30
            
        record = country.ljust(20, "#") + population.ljust(10,"#")
        outfile.seek(location)
        outfile.write(record)
        
    infile.close()
    outfile.close()

# Practice 2 Task 1
def LookupCountry():
    infile = open("NEWFILE1.TXT", "r")
    inputCountry = input("Enter a country: ").title()
    
    address = HashAsia(inputCountry) #Get address
    location = (address-1)*30 #Get location

    infile.seek(location) #Go to location of record
    country = infile.readline()[0:20].strip("#")

    collisions = 0
    while inputCountry != country:
        if address == 47:
            address = 1
            collisions += 1
        else:
            address += 1
            collisions += 1

        location = (address-1)*30
        infile.seek(location) #Go to location of record

        record = infile.readline()[0:30] #Get entire record
        country = record[0:20].strip("#") #Get country from record
        population = record[20:30].strip("#") #Get population from record

        if collisions > 47: #If number of collisions exceed maximum address, then item not found
            print("Country not found.")
            break

    if collisions <= 47:
        print("{0} with population {1} found at address {2}".format(country, population, address))
        print("Collisions:", collisions)
    
    infile.close()
    
    
