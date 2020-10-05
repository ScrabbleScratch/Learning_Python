#ask for birth date
while True:
    date = input('Enter your birth date (YYYYMMDD): ')
    if date.isnumeric(): break

#add the numbers until one digit
while len(date) > 1:
    sum = 0
    for i in date:
        sum += int(i)
        date = str(sum)

#print result
print('Your digit of life is: ',date)