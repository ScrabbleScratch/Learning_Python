#ask for text
text = input('Enter text: ').lower()

#remove spaces
text = text.replace(' ','')

#check each character
if len(text):
    counter = -1
    for i in range(len(text)//2):
        if text[i] != text[counter]:
            print('It is not a palindrome')
            break
        counter -= 1
    else:
        print('It is a palindrome')
else:
    print('It is not a palindrome')



# a small way to do it

if text == text[::-1] and len(text):
    print('It is a palindrome')
else:
    print('It is not a palindrome')