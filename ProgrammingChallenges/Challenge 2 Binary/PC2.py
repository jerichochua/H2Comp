class stack: #Task 1
    def __init__(self):
        self.data = [] #Initialise empty list

    def __str__(self):
        text = ""
        for i in range(len(self.data)-1, -1, -1):
            text = text + "{}".format(self.data[i])
        return text

    def isEmpty(self): #Chcek if stack is empty
        return len(self.data) == 0

    def push(self, data): #Push an item into the stack
        self.data.append(data)

    def pop(self): #Pop an item out of the stack
        return self.data.pop()

    def peek(self): #Look at the top of the stack
        return self.data[len(self.data)-1]

    def size(self): #Get size of the stack
        return len(self.data)

def dec_to_bin(decNumber): #Task 2 - decimal to binary
    number = stack() #Initialise stack
    quotient = decNumber
    while quotient > 0:
        remainder = quotient % 2
        number.push(remainder)
        quotient = quotient // 2

    binary = ""
    while not number.isEmpty(): #Loop until stack is empty
        binary = binary + str(number.pop())
    return binary

def testdec2bin():
    numbers = [3, 6, 9, 12, 77, 129]
    for i in range(len(numbers)):
        print("Decimal: {}".format(numbers[i]))
        print("Binary: {}".format(dec_to_bin(numbers[i])))
        print()

def dec_converter(decNumber, base): #Task 3 - decimal to octal/hexadecimal
    number = stack() #Initialise stack
    quotient = decNumber
    hexChar = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"} #Set dictionary for hex characters A-

    while quotient > 0:
        remainder = quotient % base 
        if remainder > 10:
            if remainder in hexChar: #Checks if value of remainder is A-F in hex
                number.push(hexChar[remainder])
        else:
            number.push(remainder)
        quotient = quotient // base

    newNum = ""
    while not number.isEmpty():
        newNum = newNum + str(number.pop())
    return newNum

def testdec2octhex():
    numbers = [3, 7, 8, 15, 55, 129]
    for i in range(len(numbers)):
        print("Decimal: {}".format(numbers[i]))
        print("Octal: {}, Hex: {}".format(dec_converter(numbers[i], 8), dec_converter(numbers[i], 16)))
        print()

def bin_to_dec(binNumber): #Task 4 - binary to decimal
    number = stack() #Initialise stack
    binNumber = list(str(binNumber)) #Create list of 0s/1s
    decNumber = 0
    count = 0
    
    for i in range(len(binNumber)): #Push all digits into stack
        if binNumber[i] in "23456789":
            print("Binary numbers only contain 0s and 1s!")
            return False
        number.push(binNumber[i])

    while not number.isEmpty(): #Loop until stack is empty
        digit = number.pop() #Pop a digit out of the stack
        if digit == "1": #Check if the digit is 1
            decNumber = decNumber + 2**count
            count = count + 1
        else: #Digit is 0
            count = count + 1
    return int(decNumber)

def testbin2dec():
    numbers = [1011, 10001011, 1100000010110101, 100010010010011010101011, 11111010010110101010101110101100]
    for i in range(len(numbers)):
        print("Binary: {}".format(numbers[i]))
        print("Decimal: {}".format(bin_to_dec(numbers[i])))
        print()

def anybase2decimal(number, base): #Task 5 - any base to decimal
    newNum = stack() #Intialise stack
    number = list(number)
    decNumber = 0

    if base == 2: #Binary to Decimal
        for i in range(len(number)):
            if number[i] in "23456789": #CHecks if number does not contain 0 and 1
                return False
            newNum.push(number[i]) #Push all digits into stack
        
        count = 0
        while not newNum.isEmpty(): #Loop until stack is empty
            digit = newNum.pop() #Pop a digit out of the stack
            if digit == "1": #Check if the digit is 1
                decNumber = decNumber + 2**count
                count = count + 1
            else: #Digit is 0
                count = count + 1
    
    if base == 8: #Octal to Decimal
        for i in range(len(number)):
            if number[i] in "01234567": #Checks if number contains 0-7
                newNum.push(number[i]) #Push all digits into stack
            else:
                return False
        
        count = 0
        while not newNum.isEmpty(): #Loop until stack is empty
            digit = int(newNum.pop()) #Pop a digit out of the stack
            decNumber = decNumber + (digit*(8**count)) #Calculate decimal
            count = count + 1

    if base == 16: #Hexadecimal to Decimal
        for i in range(len(number)):
            if number[i] in "0123456789ABCDEF": #Checks if number contains 0-9/A-F
                newNum.push(number[i]) #Push all digits into stack
            else:
                return False

        count = 0
        hexChar = {"A":10, "B":11, "C":12, "D":13, "E":14, "F":15} #Set dictionary for hex characters A-
        while not newNum.isEmpty(): #Loop until stack is empty
            digit = newNum.pop() #Pop a digit out of the stack
            if digit in hexChar: #Checks if digit is A-F in hex
                digit = hexChar[digit]
                decNumber = decNumber + (digit*(16**count))
                count = count + 1
            else:
                decNumber = decNumber + (int(digit)*(16**count))
                count = count + 1

    return decNumber

def testanybase2decimal():
    octal = ["10", "77", "546", "3562"]
    hexdec = ["1F", "CAD", "EBCA"]
    for i in range(len(octal)):
        print("Octal: {}".format(octal[i]))
        print("Decimal: {}".format(anybase2decimal(octal[i], 8)))
        print()
    for i in range(len(hexdec)):
        print("Hexadecimal: {}".format(hexdec[i]))
        print("Decimal: {}".format(anybase2decimal(hexdec[i], 16)))
        print()
