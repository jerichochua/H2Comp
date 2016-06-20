#Programming Challenge 1: Luhn Formula

#Task 1
    def luhn_verify(id_number):
        id_number = str(id_number)
        if not id_number.isdigit():
            return -1

        digitList = list(id_number) #Split numbers into a list
        #lastdigitPos = len(digitList)-1 #Get position of last element/check digit
        digitSum = int(digitList[len(digitList)-1])

        for i in range(len(digitList)-2, -1, -2):
            result = int(digitList[i])*2 #Multiply every other digit by 2
            if result >= 10: #Checks if result have 2 digits (10 and above)
                result = list(str(result))
                for i in range(len(result)): #Add up the 2 digits
                    digitSum += int(result[i])
            else:
                digitSum += int(result)

        for i in range(len(digitList)-3, -1, -2):
            digitSum += int(digitList[i])

        if digitSum % 10 == 0: #Checks if digit sum is divisible by 10
            return True
        else:
            return False

#Task 3
def gen_luhn(id_number):
    id_number = str(id_number)
    if not id_number.isdigit() or len(id_number) < 3:
        return -1
    else:
        digitList = list(id_number) #Split numbers into a list
        digitSum = 0

        for i in range(len(digitList)-1, -1, -2):
            result = int(digitList[i])*2 #Multiply every other digit by 2
            if result >= 10: #Checks if result have 2 digits (10 and above)
                result = list(str(result))
                for i in range(len(result)): #Add up the 2 digits
                    digitSum += int(result[i])
            else:
                digitSum += int(result)

        for i in range(len(digitList)-2, -1, -2):
            digitSum += int(digitList[i])

        checkDigit = 10 - (digitSum % 10) #Calculate the check digit of the number
        digitList.append(str(checkDigit))  #Add check digit into list of numbers
        return "".join(digitList) #Join the numbers and return it
     
def Task2():
    print(luhn_verify("asparagus"))
    print(luhn_verify("737"))
    print(luhn_verify("1762483"))
    print(luhn_verify("9781471134896"))

def Task4():
    print("Digit is", gen_luhn("234"))
    print("Digit is", gen_luhn("5813674"))
