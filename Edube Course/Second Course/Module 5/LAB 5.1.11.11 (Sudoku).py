# find each column of the array
def findcolumns(rowlist):
    columns = []
    for col in range(len(rowlist[0])):
        tcol = []
        for row in rowlist:
            tcol.append(row[col])
        columns.append(tcol)
    return columns


# find each 3x3 sub-square
def subsquares(board):
    squares = []
    boardlist = []
    for i in range(3):
        boardlist += board[i] + board[i + 3] + board[i + 6]
    for j in range(9):
        add = 3 * j
        tile = boardlist[0 + add:3 + add] + boardlist[27 + add:30 + add] + boardlist[54 + add:57 + add]
        squares.append(tile)
    return squares


# check if the sudoku is valid
def sudoku(board):
    # define a test list
    test = [str(i) for i in range(1, 10)]
    # define a variable for each element to check
    r, c, s = board, findcolumns(board), subsquares(board)
    # check if the elements meet the conditions
    for check in range(len(board)):
        if sorted((r[check])) != test or sorted(c[check]) != test or sorted(s[check]) != test:
            print('\nNO')
            break
    else:
        print('\nYES')


# ============================================================================

# ask user for data
rows = []
for i in range(9):
    # ask the user for a row until it is valid
    while True:
        row = input('Insert row %d: ' % (i + 1))
        # row needs 9 numbers specificly
        if row.isnumeric() and len(row) == 9:
            break
        print('Invalid row, try again!')
    # add row to the board
    rows.append(list(row))

# check sudoku
sudoku(rows)