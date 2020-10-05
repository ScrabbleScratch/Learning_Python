#ask for two text
text1 = input('Insert text 1: ')
text2 = input('Insert text 2: ')

#replace espaces
text1, text2 = sorted(text1.replace(' ','').lower()), sorted(text2.replace(' ','').lower())

#check if they are anagrams
if text1 == text2:
    print('Anagrams')
else:
    print('Not anagrams')