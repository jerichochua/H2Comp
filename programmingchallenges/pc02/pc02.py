#Programming Challenge 2: Binary Representation

#Task 1
class stack:
    def __init__(self):
        self.data = []

    def __str__(self):
        text = ""
        for i in range(len(self.data)-1, -1, -1):
            text = text + "{}".format(self.data[i])
        return text

    def isEmpty(self):
        """Returns True if stack is empty, False otherwise"""
        return len(self.data) == 0

    def push(self, data):
        """Push data into stack"""
        self.data.append(data)

    def pop(self):
        """Pop top data out of stack"""
        return self.data.pop()

    def peek(self):
        """Returns top of stack"""
        return self.data[len(self.data)-1]

    def size(self):
        """Returns size of stack"""
        return len(self.data)

#Task 2 - decimal to binary
def dec_to_bin(decNumber):
    number = stack()
    while decNumber > 0:
        remainder = decNumber % 2
        number.push(remainder)
        decNumber = decNumber // 2

    binary = ""
    while not number.isEmpty():
        binary = binary + str(number.pop())

    return binary

def Evidence3():
    numbers = [3, 6, 9, 12, 77, 129]
    for i in range(len(numbers)):
        print("Decimal: {}".format(numbers[i]))
        print("Binary: {}".format(dec_to_bin(numbers[i])))
        print()

#Task 3 - decimal to octal/hexadecimal
def dec_converter(decNumber, base):
    number = stack()
    hexChar = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}

    while decNumber > 0:
        remainder = decNumber % base 
        if remainder > 10:
            if remainder in hexChar: #Checks if value of remainder is A-F in hex
                number.push(hexChar[remainder])
        else:
            number.push(remainder)
        decNumber = decNumber // base

    newNumber = ""
    while not number.isEmpty():
        newNumber = newNumber + str(number.pop())
    return newNumber

def Evidence5():
    numbers = [3, 7, 8, 15, 55, 129]
    for i in range(len(numbers)):
        print("Decimal: {}".format(numbers[i]))
        print("Octal: {}, Hex: {}".format(dec_converter(numbers[i], 8), dec_converter(numbers[i], 16)))
        print()

#Task 4 - binary to decimal
def bin_to_dec(binNumber):
    number = stack()
    binNumber = list(str(binNumber))
    decNumber = 0
    count = 0
    
    for i in range(len(binNumber)): #Push all digits into stack
        if binNumber[i] in "23456789":
            print("Binary numbers only contain 0s and 1s!")
            return False
        number.push(binNumber[i])

    while not number.isEmpty(): #Loop until stack is empty
        digit = number.pop()
        if digit == "1": #Check if the digit is 1
            decNumber = decNumber + 2**count
            count = count + 1
        else: #Digit is 0
            count = count + 1
    return int(decNumber)

def Evidence7():
    BINARY = [1011, 10001011, 1100000010110101, 100010010010011010101011, 11111010010110101010101110101100]
    for i in range(len(BINARY)):
        print("Binary: {}".format(BINARY[i]))
        print("Decimal: {}".format(bin_to_dec(BINARY[i])))
        print()

#Task 5 - any base to decimal
def anybase2decimal(number, base): 
    newNumber = stack()
    number = list(number)
    decNumber = 0
    
    if base == 8: #Octal to Decimal
        for i in range(len(number)):
            if number[i] in "01234567": #Checks if number contains 0-7
                newNumber.push(number[i]) #Push all digits into stack
            else:
                return False
        
        count = 0
        while not newNumber.isEmpty(): #Loop until stack is empty
            digit = int(newNumber.pop()) #Pop a digit out of the stack
            decNumber = decNumber + (digit*(8**count)) #Calculate decimal
            count = count + 1

    if base == 16: #Hexadecimal to Decimal
        hexChar = {"A":10, "B":11, "C":12, "D":13, "E":14, "F":15}

        for i in range(len(number)):
            if number[i] in "0123456789ABCDEF": #Checks if number contains 0-9/A-F
                newNumber.push(number[i]) #Push all digits into stack
            else:
                return False

        count = 0
        while not newNumber.isEmpty(): #Loop until stack is empty
            digit = newNumber.pop() #Pop a digit out of the stack
            if digit in hexChar: #Checks if digit is A-F in hex
                digit = hexChar[digit]
                decNumber = decNumber + (digit*(base**count))
            else:
                decNumber = decNumber + (int(digit)*(base**count))
            count = count + 1

    return decNumber

def Evidence9():
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
