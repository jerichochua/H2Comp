# Programming Challenge 12: Rot13

scrambled = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
unscrambled = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'

infile = open('rot13.txt', 'r')

for line in infile:
    line = line.rstrip()
    newstring = ''
    for letter in line:
        if letter in scrambled:
            newstring += unscrambled[scrambled.index(letter)]
        else:
            newstring += letter

    print(newstring)

infile.close()
