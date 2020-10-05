def char_count(text, char):
    count = 0
    for c in text:
        if c == char:
            count += 1
    return count

filename = input("Enter the file name to analyze: ")

with open(filename) as f:
    text = f.read()
    
for char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789":
    perc = 100 * char_count(text, char) / len(text)
    print("{0} - {1}%".format(char, round(perc, 2)))
