def luhn_verify(id_number):
    if id_number.isalpha(): #Check if id_number contains alphabets
        return False
    numlist = list(id_number) #Split numbers into a list
    lastdigitPos = len(numlist)-1 #Get position of last element/check digit
    digitSum = int(numlist[lastdigitPos])

    for i in range(len(numlist)-2, -1, -2):
        result = int(numlist[i])*2 #Multiply every other digit by 2
        if result >= 10: #Checks if result have 2 digits (10 and above)
            result = list(str(result))
            for i in range(len(result)): #Add up the 2 digits
                digitSum += int(result[i])
        else:
            digitSum += int(result)

    for i in range(len(numlist)-3, -1, -2):
        digitSum += int(numlist[i])

    if digitSum % 10 == 0: #Checks if digit sum is divisible by 10
        return True
    else:
        return False
        
def main1():
    print(luhn_verify("asparagus"))
    print(luhn_verify("737"))
    print(luhn_verify("1762483"))
    print(luhn_verify("9781471134896"))

def gen_luhn(id_number):
    if len(id_number) < 3: #Check if minimum 3 digits have been entered
        print("Minimum 3 digits needed!")
        return False
    else:
        numlist = list(id_number) #Split numbers into a list
        lastdigitPos = len(numlist)-1 #Get position of last element/check digit
        digitSum = 0

        for i in range(len(numlist)-1, -1, -2):
            result = int(numlist[i])*2 #Multiply every other digit by 2
            if result >= 10: #Checks if result have 2 digits (10 and above)
                result = list(str(result))
                for i in range(len(result)): #Add up the 2 digits
                    digitSum += int(result[i])
            else:
                digitSum += int(result)

        for i in range(len(numlist)-2, -1, -2):
            digitSum += int(numlist[i])

        checkDigit = 10 - (digitSum % 10) #Calculate the check digit of the number
        numlist.append(str(checkDigit))  #Add check digit into list of numbers
        return "".join(numlist) #Join the numbers and return it

def main():
    print("Digit is", gen_luhn("234"))
    print("Digit is", gen_luhn("5813674"))

main()
