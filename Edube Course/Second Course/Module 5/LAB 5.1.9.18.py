def mysplit(strng):
    size = len(strng)
    ls = []
    word = ''
    for i in range(size):
        if strng[i] != ' ':
            word += strng[i]
        elif strng[i] == ' ':
            if word != '':
                ls.append(word)
            word = ''
    if word != '':
        ls.append(word)
    word = ''
    return ls


print(mysplit("To be or not to be, this is a question"))
print(mysplit("To be or not to be,this is a question"))
print(mysplit("   "))
print(mysplit(" abc "))
print(mysplit(""))