#!/usr/bin/env python3

"""
Program to encrypt text using the Caesar Cipher method.
It uses the Digit of Life to create a custom shift value.
It also reverts the order of the characters (last will
be the first).

Note: It does encrypt symbols nor numbers.
Encryption is not fully compatible with V1.
"""

#main menu
def mainMenu():
    #action to be done
    print('\n'
          '****************************\n'
          '*     SELECT AN OPTION     *\n'
          '*        1) Encrypt        *\n'
          '*        2) Decrypt        *\n'
          '****************************\n')
    while True:
        option = input('Select: ')
        if option == '1' or option == '2': break
        print('Insert a valid option!!')

    #shift value to use for encrypt or decrypt
    print('\n'
          '****************************\n'
          '*     SELECT AN OPTION     *\n'
          '*     1) Insert shift      *\n'
          '*     2) Create shift      *\n'
          '****************************\n')
    while True:
        shiftOption = input('Select: ')
        if shiftOption == '1' or shiftOption == '2': break
        print('Insert a valid option!!')
    if shiftOption == '1':
        while True:
            shiftVal = input('\nInsert shift (max 26): ')
            if shiftVal.isnumeric() and int(shiftVal)>0 and int(shiftVal)<=25: break
            print('Insert a valid shift value!!')
    #shift value created with The Digit of Life
    elif shiftOption == '2':
        while True:
            date = input('\nInsert your birth date (ddmmyyyy): ')
            if len(date) == 8 and date.isnumeric():
                while len(date) > 1:
                    sum = 0
                    for i in date:
                        sum += int(i)
                        date = str(sum)
                shiftVal = sum
                break
            print('Insert a valid date!!')
    #print shift value to be used
    print('Shift value = %s\n' % shiftVal)
    #text to be processed
    text = input('Insert text: ')

    #call the operation to be done
    if option == '1': print('\nENCRYPTED TEXT: ',encrypt(shiftVal, text))
    else: print('\nDECRYPTED TEXT: ',decrypt(shiftVal, text))
    return

#function to encrypt, it requires a shift value and text
def encrypt(shift, text):
    shift = int(shift)
    encrypted = ''
    for char in text:
        newchar = ord(char)
        if char.isalpha():
            newchar += shift
            if char.islower() and newchar > 122: newchar -= 26
            elif char.isupper() and newchar > 90: newchar -= 26
            newchar = chr(newchar)
        elif newchar>=32 and newchar<=64:
            newchar += shift
            if newchar > 64: newchar -= 33
            newchar = chr(newchar)
        else: newchar = char
        encrypted += newchar
    encrypted = encrypted[::-1]
    return encrypted

#function to decrypt, it requires a shift value and text
def decrypt(shift, text):
    shift = int(shift)
    decrypted = ''
    for char in text:
        newchar = ord(char)
        if char.isalpha():
            newchar -= shift
            if char.islower() and newchar < 97: newchar += 26
            elif char.isupper() and newchar < 65: newchar += 26
            newchar = chr(newchar)
        elif newchar >= 32 and newchar <= 64:
            newchar -= shift
            if newchar < 32: newchar += 33
            newchar = chr(newchar)
        else: newchar = char
        decrypted += newchar
    decrypted = decrypted[::-1]
    return decrypted

#main loop
while True:
    mainMenu()
    if 'y' in input('\nExit? (y/n): ').lower(): break