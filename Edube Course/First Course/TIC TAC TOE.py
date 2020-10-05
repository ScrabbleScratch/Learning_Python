from random import randrange

userWin, pcWin = False, False

gameBoard = [[1,2,3],\
             [4,5,6],\
             [7,8,9]]

boardSquares = ((0,0),(0,1),(0,2),\
                (1,0),(1,1),(1,2),\
                (2,0),(2,1),(2,2))


def DisplayBoard(board):
#
# the function accepts one parameter containing the board's current status
# and prints it out to the console
#
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|  ',board[0][0],'  |  ',board[0][1],'  |  ',board[0][2],'  |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|  ',board[1][0],'  |  ',board[1][1],'  |  ',board[1][2],'  |')
    print('|       |       |       |')
    print('+-------+-------+-------+')
    print('|       |       |       |')
    print('|  ',board[2][0],'  |  ',board[2][1],'  |  ',board[2][2],'  |')
    print('|       |       |       |')
    print('+-------+-------+-------+')


def EnterMove(board):
#
# the function accepts the board current status, asks the user about their move, 
# checks the input and updates the board according to the user's decision
#
    userMove = int(input('Enter your move: '))
    
    while True:
        
        if userMove > 0 and userMove < 10 and boardSquares[userMove-1] in board:
            r = boardSquares[userMove-1][0]
            c = boardSquares[userMove-1][1]
            gameBoard[r][c] = 'O'
            break
        else: userMove = int(input('Enter a valid move: '))
        
    DisplayBoard(gameBoard)

    return


def MakeListOfFreeFields(board):
#
# the function browses the board and builds a list of all the free squares; 
# the list consists of tuples, while each tuple is a pair of row and column numbers
#
    freeFields = []
    for i in range(3):
        for j in range(3):
            if board[i][j] != 'X' and board[i][j] != 'O':
                freeFields.append((i,j))
    return freeFields


def VictoryFor(board, sign):
#
# the function analyzes the board status in order to check if 
# the player using 'O's or 'X's has won the game
#
    for i in range(3):
        if (board[i][0] == sign and board[i][1] == sign and board[i][2] == sign)\
           or (board[0][i] == sign and board[1][i] == sign and board[2][i] == sign):
            return True

    if (board[0][0] == sign and board[1][1] == sign and board[2][2] == sign)\
       or (board[2][0] == sign and board[1][1] == sign and board[0][2] == sign):
        return True
    else:
        return False


def DrawMove(board):
#
# the function draws the computer's move and updates the board
#
    move = randrange(8)

    if len(board) > 0:
        while True:
            
            if boardSquares[move] in board:
                r = boardSquares[move][0]
                c = boardSquares[move][1]
                gameBoard[r][c] = 'X'
                break
            else:
                move = randrange(8)

    DisplayBoard(gameBoard)

    return


#---------------------------------------------------------------------------------------------------


DisplayBoard(gameBoard)

while True:
    
    EnterMove(MakeListOfFreeFields(gameBoard))
    
    if VictoryFor(gameBoard,'O'):
        print('You Won')
        break
    
    DrawMove(MakeListOfFreeFields(gameBoard))

    if VictoryFor(gameBoard,'X'):
        print('PC Won')
        break

input()
