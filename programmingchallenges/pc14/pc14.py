# Programming Challenge 14 - Cipher

infile = open('cipher.txt', 'r')

keyphrase = infile.readline().rstrip()
cipher = ''

# Get alphabets
alphabets = ''
for i in range(26):
    if chr(97+i) not in alphabets:
        alphabets += chr(97+i)

# Get key phrase without repeated letters
for letter in keyphrase:
    letter = letter.upper()
    if letter not in cipher:
        cipher += letter

keyphrase = cipher

# Insert remaining letters into cipherList
for i in range(26):
    if chr(65+i) not in cipher:
        cipher += chr(65+i)

# Decrypt message
newstring = ''
for line in infile:
    line = line.rstrip()
    for letter in line:
        if letter in cipher:
            newstring += alphabets[cipher.index(letter)]
        else:
            newstring += letter

# Display output
print('***')
print(keyphrase)
print(newstring)
print('***')

infile.close()
