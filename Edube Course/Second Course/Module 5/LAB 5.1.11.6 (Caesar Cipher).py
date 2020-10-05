#asking for data
text = input('Please insert the text to encrypt: ')
while True:
    try:
        shift = int(input('\nEnter the shifting value (1-25): '))
        if shift >= 1 and shift <= 25:
            break
        else:
            print('The value entered is out of range!')
    except:
        print('The value entered is not valid! Please try again!')

#creating empty encrypted string
output = ''

#encrypting text
for char in text:
    if char.isalpha():
        newchar = ord(char) + shift
        if char.islower() and newchar > 122:
            newchar -= 26
        elif char.isupper() and newchar > 90:
            newchar -= 26
        newchar = chr(newchar)
    else:
        newchar = char
    output += newchar

#print the encrypted string
print(output)