# Shaun Leung
# Dec 23, 2021
""""
Ahhh the N Queens problem. I actually did this one in my AI class at the U of S
It was a bit different than the question asked here in that it was programming
dueling AI in an N Queens's type game where the last player to place a queen win
wins, I will add the files to this folder.

So the big thing here is back tracking since we will need to check lots of 
different board states we will want to bail on any invalid board states ASAP.

We will have to build some helper functions to make things a bit more readable 
such as checking board state validity and dealing with diagonals. 
"""
import copy  # going to need to do some deep copies here for the board states
"""
function to set up the board for N Queens
X's are empty spaces
Q's are Queens
"""


def nQueens(n):
    board = [['X' for i in range(n)] for j in range(n)]
    # try adding queens to the first file
    return addQueen(board, 0)


"""
recursively adds Queens to the board then check is the board is in a valid state
to continue. if it isnt then that branch is dead and it continues on
"""


def addQueen(board, file):
    newBoard = copy.deepcopy(board)
    succeses = 0
    # check if queen can be added
    # add queens
    for rank in range(len(board)):
        newBoard = copy.deepcopy(board)
        newBoard[rank][file] = 'Q'
        if isValid(newBoard):
            if file + 1 == len(board):
                succeses += 1
            else:
                succeses += addQueen(newBoard, file+1)

    return succeses


"""
Checks to see if the board is in a valid state
"""


def isValid(board):
    n = len(board)
    queens = []
    for i, row in enumerate(board):
        for j, col in enumerate(row):
            if col == 'Q':
                queens.append((i, j))

    for queen in queens:
        if attacking(board, queen):
            return False

    return True


"""
This function will check to see if a queen is attacking another queen. which 
is an invalic board state. 

If you are not familiar with Chess ranks are rows and files are columns so we
can use that nomenclature here for clarity. 
"""


def attacking(board, queen):
    rank = queen[0]
    file = queen[1]
    # Check rank
    for i, square in enumerate(board[rank]):
        if square == 'Q' and i != file:
            return True

    # Check file
    for i, square in enumerate(board):
        if square[file] == 'Q' and i != rank:
            return True

    # check diagonal
    # check NW->SE
    offset = min(rank, file)
    i = rank - offset
    j = file - offset
    while i < len(board) and j < len(board):
        if board[i][j] == 'Q' and (i != rank and j != file):
            return True

        i += 1
        j += 1

    # check NE->SW
    offset = min(rank, (len(board)-1-file))
    i = rank - offset
    j = file + offset

    while i < len(board) and j >= 0:
        if board[i][j] == 'Q' and (i != rank and j != file):
            return True

        i += 1
        j -= 1

    return False


# tests
print(nQueens(1))
print(nQueens(2))
print(nQueens(3))
print(nQueens(4))
# Was kinda thrown off by this larger n test but after looking it up it's right
print(nQueens(8))
