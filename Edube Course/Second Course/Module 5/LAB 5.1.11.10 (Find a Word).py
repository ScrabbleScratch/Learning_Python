#ask for data
word = input('Enter a word to find: ').lower()
text = input('Enter a combination of characters: ').lower()

#create a variable to save current position
pos = 0

#check if the word exists within the text
for char in word:
    pos = text.find(char,pos)
    if pos == -1:
        print('Word not found!')
        break
else:
    print('Word found!')