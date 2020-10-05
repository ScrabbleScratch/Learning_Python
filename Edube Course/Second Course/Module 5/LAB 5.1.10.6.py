numbers = (('###','# #','# #','# #','###'),\
           ('  #','  #','  #','  #','  #'),\
           ('###','  #','###','#  ','###'),\
           ('###','  #','###','  #','###'),\
           ('# #','# #','###','  #','  #'),\
           ('###','#  ','###','  #','###'),\
           ('###','#  ','###','# #','###'),\
           ('###','  #','  #','  #','  #'),\
           ('###','# #','###','# #','###'),\
           ('###','# #','###','  #','###'))

def display(digits):
    str = ['','','','','']
    output = ''
    for i in digits:
        str[0] += numbers[int(i)][0] + ' '
        str[1] += numbers[int(i)][1] + ' '
        str[2] += numbers[int(i)][2] + ' '
        str[3] += numbers[int(i)][3] + ' '
        str[4] += numbers[int(i)][4] + ' '
    for j in str:
        output += j + '\n'
    return output

print(display(input('Insert a number: ')))