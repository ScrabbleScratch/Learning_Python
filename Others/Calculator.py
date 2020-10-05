while True:
    print("""Options:
    Enter "sumar" to add two numbers
    Enter "restar" to subtract two numbers
    Enter "multiplicar" to multiply two numbers
    Enter "dividir" to divide two numbers
    Enter "quit" to exit""")
    user_input = input(':')

    if user_input == 'quit':
        break
    elif user_input == 'sumar':
        num1 = float(input('Number 1: '))
        num2 = float(input('Number 2: '))
        result = str(num1 + num2)
    elif user_input == 'restar':
        num1 = float(input('Number 1: '))
        num2 = float(input('Number 2: '))
        result = str(num1 - num2)
    elif user_input == 'multiplicar':
        num1 = float(input('Number 1: '))
        num2 = float(input('Number 2: '))
        result = str(num1 * num2)
    elif user_input == 'dividir':
        num1 = float(input('Number 1: '))
        num2 = float(input('Number 2: '))
        result = str(num1 / num2)
    else:
        print('Unknown Input')

    print('The result is: ' + result)
