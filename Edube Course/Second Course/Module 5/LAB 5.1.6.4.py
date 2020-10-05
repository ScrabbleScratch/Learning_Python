def readint(prompt, min, max):
    global n
    try:
        n = int(input(prompt))
        if n < min or n > max:
            print('Error: the value is not within permitted range (',min,'..',max,')')
            readint(prompt, min, max)
    except:
        print('Error: wrong input')
        readint(prompt, min, max)
    return n

v = readint("Enter a number from -10 to 10: ", -10, 10)

print("The number is:", v)